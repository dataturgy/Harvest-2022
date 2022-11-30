import bonobo
import psycopg2
import os 
from bonobo.config import use

@use('postgres_app')
def load_customer_order(customer_nr, article_nr, order_amount, **args):
    try:
        cursor = args['postgres_app'].cursor()
        cursor.execute("INSERT INTO customer_order (customer_nr, article_nr, order_amount) VALUES(%s, %s, %s)", 
        (customer_nr, article_nr, order_amount))
        args['postgres_app'].commit()
        cursor.close()
    except psycopg2.errors.UniqueViolation:
        # I made an error in the generation of the demo set. This hides this...
        args['postgres_app'].rollback()
    except Exception as e: 
        args['postgres_app'].rollback()
        raise e 

def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(
        bonobo.CsvReader('customer_order.csv', fs='fs.data'),
        load_customer_order
    )

    return graph


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    mongo_app = None
    postgres_app = psycopg2.connect(
        host="localhost",
        database="app",
        user="app",
        password="app")
    postgres_dwh = psycopg2.connect(
        host="localhost",
        database="dwh",
        user="dwh",
        password="dwh")

    file_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+f'{os.path.sep}..{os.path.sep}..{os.path.sep}data')
    return {
        'mongo_app': mongo_app,
        'postgres_app': postgres_app,
        'postgres_dwh': postgres_dwh,
        'fs.data': bonobo.open_fs(file_dir),
    }

# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )