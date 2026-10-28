import argparse
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(
    filename="converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def convert_csv_to_excel(input_file, output_file):
    try:
        input_path = Path(input_file)
        output_path = Path(output_file)

        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        if input_path.suffix.lower() != ".csv":
            raise ValueError("Input file must have a .csv extension.")

        if output_path.suffix.lower() != ".xlsx":
            raise ValueError("Output file must have a .xlsx extension.")

        logging.info("Starting conversion: %s", input_file)

        df = pd.read_csv(input_path)

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        df = df.drop_duplicates()

        if "city" in df.columns:
            df["city"] = df["city"].fillna("Unknown")

        if "marks" in df.columns:
            df["marks"] = df["marks"].fillna(0)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(output_path, index=False)

        logging.info("Conversion successful: %s", output_file)
        print(f"Success! Excel file saved to: {output_file}")

    except (FileNotFoundError, ValueError, pd.errors.EmptyDataError,
            pd.errors.ParserError, PermissionError) as error:
        logging.error("Conversion failed: %s", error)
        print(f"Error: {error}")

    except Exception:
        logging.exception("Unexpected error during conversion")
        print("Error: An unexpected error occurred. Check converter.log for details.")


def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV files to Excel with data cleaning."
    )
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("output", help="Path to output Excel file")

    args = parser.parse_args()
    convert_csv_to_excel(args.input, args.output)


if __name__ == "__main__":
    main()
