# Move to the directory
cd pipeline/tests
# Set up
curl -O -# https://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/hourly/h765a.csv
mkdir -p output
mkdir -p output/plots
# Run the pipeline
pipeline
# Clean up
rm h765a.csv
# Go back to the root directory
cd ../..