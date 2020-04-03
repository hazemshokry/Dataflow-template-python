import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

"""
The starter example show how to build and deploy a dataflow templated job.
This example receive CSV input file '--input' as an argument, parse it and count number of countries.
"""

class StarterOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        # Use add_value_provider_argument for arguments to be templatable
        parser.add_value_provider_argument(
            '--input',
            default='input/covid_19_data.csv',
            help='Path of the file to read from')


def run():
    pipeline_options = PipelineOptions()
    p = beam.Pipeline(options=pipeline_options)
    wordcount_options = pipeline_options.view_as(StarterOptions)

    input = (
            p | 'read' >> beam.io.ReadFromText(wordcount_options.input, skip_header_lines=1)
            | 'Emit <country, 1>' >> beam.Map(lambda x: (x.split(',')[3], 1))
            | 'Group by country' >> beam.CombinePerKey(sum))

    output = input | beam.io.WriteToText("output")

    p.run()

if __name__ == '__main__':
    run()


