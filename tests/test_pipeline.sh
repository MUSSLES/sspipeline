# Move to the test directory
cd tests
# Set up
curl -O -# https://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/hourly/h765a.csv
mkdir -p output
# Run the pipeline
pipeline
# Clean up
rm h765a.csv
# Go back to the root directory
cd ..