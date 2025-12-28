# Import libraries
# argparse → handles command-line arguments
# SparkSession → entry point to Spark functionality
# F → alias for pyspark.sql.functions for transformations
import argparse
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# ------------------------------
# Parse command-line arguments
# ------------------------------
# Create a parser with a description of what the script does

comment = """
This script is meant to be reusable and flexible, not hard-coded to a single dataset or environment.
Instead of editing the Python code every time you want to change:

the listings file path

the reviews file path

the output directory

you can simply pass them when running the script, like:

spark-submit popular_listings.py --listings /data/listings.csv --reviews /data/reviews.csv --output /results/popular_listings

This makes the script:

usable in different environments (local, cluster, cloud)
compatible with automation (Airflow, cron, CI/CD, Databricks jobs)
safer (no editing code → fewer mistakes)
more professional and production-ready


"""

parser = argparse.ArgumentParser(description='Most popular listings parameters')

# Define expected command-line arguments
parser.add_argument('--listings', help='Path to the listings dataset')
parser.add_argument('--reviews', help='Path to the reviews dataset')
parser.add_argument('--output', help='Directory to save the output')

# Parse the input arguments from the command line
args = parser.parse_args()

# ------------------------------
# Create Spark Session
# ------------------------------
# SparkSession is the main entry point to work with Spark
spark = SparkSession.builder \
    .appName("Most popular listings") \
    .getOrCreate()

# ------------------------------
# Load Listings Dataset
# ------------------------------
# Reads a CSV file into a Spark DataFrame
# header=True → first row contains column names
# inferSchema=True → automatically detect column data types
# sep, quote, escape, multiLine settings → ensure correct handling of CSV formatting
# mode="PERMISSIVE" → Spark will not fail if it encounters malformed rows

listings = spark.read.csv(args.listings,
    header=True,
    inferSchema=True,
    sep=",",
    quote='"',
    escape='"',
    multiLine=True,
    mode="PERMISSIVE"
)

# ------------------------------
# Load Reviews Dataset
# ------------------------------
# Same CSV reading configuration applied to reviews dataset

reviews = spark.read.csv(args.reviews,
    header=True,
    inferSchema=True,
    sep=",",
    quote='"',
    escape='"',
    multiLine=True,
    mode="PERMISSIVE"
)

# ------------------------------
# Join Listings with Reviews
# ------------------------------
# Inner join → keep only listings that actually have reviews
# Match records where listing.id = reviews.listing_id
listings_reviews = listings.join(
    reviews, listings.id == reviews.listing_id, how='inner'
)

# ------------------------------
# Count Number of Reviews Per Listing
# ------------------------------
# Group by listing ID and name
# Count how many reviews each listing has
# Order results from most reviewed → least reviewed

reviews_per_listing = (
    listings_reviews 
    .groupBy(listings.id, listings.name) 
    .agg(
    F.count(reviews.id).alias('num_reviews')
    ) 
  .orderBy('num_reviews', ascending=False) 
  )

# ------------------------------
# Save Output
# ------------------------------
# Writes result as CSV to the specified output directory
# header=True → include column headers in output

reviews_per_listing.write.csv(
    args.output,
    header=True,
    )