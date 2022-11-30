CREATE TABLE "customer" (
  "customer_nr" SERIAL PRIMARY KEY,
  "customer_name" varchar,
  "customer_address" varchar,
  "customer_city" varchar
);

CREATE TABLE "customer_order" (
  "customer_nr" int,
  "article_nr" int,
  "order_amount" int,
  PRIMARY KEY ("customer_nr", "article_nr")
);

CREATE TABLE "article" (
  "article_nr" int PRIMARY KEY,
  "article_name" varchar,
  "article_price" NUMERIC(12, 2),
  "article_warehouse" int,
  "article_shelf" int
);

ALTER TABLE "customer_order" ADD FOREIGN KEY ("customer_nr") REFERENCES "customer" ("customer_nr");

ALTER TABLE "customer_order" ADD FOREIGN KEY ("article_nr") REFERENCES "article" ("article_nr");
