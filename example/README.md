# SSPipeline Example

## Motivation

We at MUSSLES thought that it would be extremely useful, for the user of SSPipeline, if there was a demo for our SSPipeline package. So, we have put together an example which uses the [Grand Isle, Louisiana, USA](https://uhslc.soest.hawaii.edu/rqds/atlantic/doc/qa765a.dmt) data set from the University of Hawaii Sea Level Center (UHSLC). We chose this data set because not only does it barely have any gaps, but it also only takes roughly 5 minutes to run on an average computer.

## Directory Structure

./

- example "home" directory

./configs/

- home of the different configuration files for the example

./data/

- directory for the data set used in the example

./output/

- output directory for the example

## Usage

The [`bootstrap.sh`](bootstrap.sh) file is the script that you will want to run everything from. To see exactly what this script does, you can run the following to get the usage message:

```sh
bash bootstrap.sh --help
```

If you want to just solely run the example:

```sh
bash bootstrap.sh run
```

Note that if you want to play around with the parameters with which the example uses to fit the data set, check out this [file](configs/config.json). See more in the [Customization](#customization) section.

## Customization

A full blown configuration file for SSPipeline should look something along the lines of:

```json
{
  "adaption": 300,
  "data": "data/h765a.csv",
  "iterations": 3000,
  "output_dir": "output",
  "percentage": 0.9,
  "plot": 1,
  "sequences": 3,
  "transition": [10, 2, 0.01],
  "verbose": 1
}
```

You can change all of these configurations to fit your preferences, however, some of them have a more drastic effect on your output than others do. TODO

## Results

**Diagnostic Plots:** [link](output/plots/diagnostic_plots.png)

![Diagnostic Plot](output/plots/diagnostic_plots.png)

**Other Plots:** [link to folder](output/plots)

- [ACF Function](output/plots/acf_function.png)
- [Annual Maximum](output/plots/annual_maximum.png)
- [Cleaned Data](output/plots/cleaned_data.png)
- [GR Diagnostic](output/plots/gr_diagnostic.png)
- [History Plots](output/plots/history_plots.png)
- [Parameter Pool](output/plots/params_pool.png)

**Calibrated Parameters:** [link to folder](output/parameters)

- [Parameter 1](output/parameters/parameter-1.txt)
- [Parameter 2](output/parameters/parameter-2.txt)
- [Parameter 3](output/parameters/parameter-3.txt)

**Return Levels:** [link](output/return_levels.csv)

**Log:** [link](output/sspipeline.log)
