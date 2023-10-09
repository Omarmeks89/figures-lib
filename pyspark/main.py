from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()


prod_df = spark.createDataFrame(
        [
            ("prod1", ),
            ("prod2", ),
            ("prod3", ),
            ("prod4", ),
            ],
        schema="product string",
        )


relation_df = spark.createDataFrame(
        [
            ("A", "prod1", ),
            ("B", "prod1", ),
            ("C", "prod1", ),
            ("A", "prod2", ),
            ("A", "prod3", ),
            ("B", "prod2", ),
            ("C", "prod3", ),
            ("D", "prod1", ),
            ("D", "prod2", ),
            ("D", "prod3", ),
            ("E", "prod3", ),
            ],
        schema="category string, product string",
        )


def main() -> None:
    """relation_fd implements <many-to-many> relation
    between product and category, we can think about like:
        <category FOREIGN_KEY category.name,
        product FOREIGN_KEY prod_df.product>
    so, this case (i think) we needn`t have implement
    DF <category> because anyway we will use relation-table
    (this task) to create final DF <product:category>.
    I hope it`s right solution=)
    """
    relation_df.join(prod_df, ["product"], how="fullouter").show()

    # or (result will be the same):
    prod_df.join(relation_df, ["product"], how="leftouter").show()


if __name__ == "__main__":
    main()
