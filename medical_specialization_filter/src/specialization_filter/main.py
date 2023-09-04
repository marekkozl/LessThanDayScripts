import argparse
import logging
import sys
from pathlib import Path

import specialization_filter.utils.log as log
from specialization_filter.core.data_frame import DataFrameParser
from specialization_filter.parsers.lower_silesian_parser import LowerSilesianParser
from specialization_filter.parsers.masovian_parser import MasovianParser
from specialization_filter.parsers.place_parser import PlaceParser
from specialization_filter.parsers.pomeranian_parser import PomeranianParser
from specialization_filter.parsers.silesian_parser import SilesianParser

logger = logging.getLogger(__name__)


def process_command_line():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    setup_parser(parser)
    return parser.parse_args()


def setup_parser(root_parser: argparse.ArgumentParser):
    root_parser.add_argument(
        "--input_dir",
        type=Path,
        default=None,
        help="Path to input csv's directory",
    )
    root_parser.add_argument(
        "--output_dir",
        type=Path,
        default=None,
        help="Output directory",
    )
    log.setup_parser(root_parser)


def main(args=None):
    if args is None:
        args = process_command_line()
    log.setup_logging(args.logging_level)
    logger.debug("Arguments: %s", args)
    place_parser = PlaceParser(args.input_dir)
    dfp = DataFrameParser(place_parser)
    pomorze_specializations = PomeranianParser(args.input_dir).run()
    dfp.add_specializations("Pomorskie", pomorze_specializations)

    mazowieckie_spec = MasovianParser(args.input_dir).run()
    dfp.add_specializations("Mazowieckie", mazowieckie_spec)

    slaskie_spec = SilesianParser(args.input_dir).run()
    dfp.add_specializations("Slaskie", slaskie_spec)

    dolnoslaskie_spec = LowerSilesianParser(args.input_dir).run()
    dfp.add_specializations("Dolnoslaskie", dolnoslaskie_spec)
    dfp.save(args.output_dir)


if __name__ == "__main__":
    sys.exit(main())
