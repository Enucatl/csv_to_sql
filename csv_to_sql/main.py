import re
import click
import pandas as pd


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.File("w"))
@click.option("--table_name", default="data")
def main(input_file, output_file, table_name):
    df = pd.read_csv(input_file)
    create_statement = pd.io.sql.get_schema(df, name=table_name)
    output_file.write(create_statement)
    output_file.write(";\n\n")
    output_file.write(
        f'INSERT INTO "{table_name}" ({",".join(df.columns)}) \n \n VALUES \n'
    )                                                       
    values_string = [
            str(row).replace("nan", "NULL")
            for row in df.itertuples(index=False, name=None)
    ]
    output_file.write("\n,".join(values_string))
    output_file.write(";")


if __name__ == "__main__":
    main()
