import argparse
from pathlib import Path

from .inference import full_pipe


def inference():
    print("doing inference")
    args = get_inference_args()
    full_pipe.main(
        args.input_path,
        args.output_dir,
        args.spans_model,
        args.labels_model,
        args.verbose,
        args.dry,
    )


def train():
    print("doing training")


def get_inference_args():
    """
    handles the argument parsing, when full_pipe.py is run from the commandline
    return:
        parsed commandline arguments
    """
    arg_par = argparse.ArgumentParser()
    arg_par.add_argument(
        "--input_path",
        "-i",
        # default=Path("./data/genres_original/"),
        type=Path,
        help="path to the data directory containing the "
        + "text files, or singular text file, to process .",
    )
    arg_par.add_argument(
        "--output_dir",
        "-o",
        # default=Path("./data/lyrics_original/"),
        type=Path,
        help="path to the directory to save the output.",
    )
    arg_par.add_argument(
        "--spans_model",
        "-s",
        default="Theoreticallyhugo/longformer-spans",
        type=str,
        help="model to use for finding the spans."
        + "either path to local model or path of huggingface repository"
        + 'in the format of "user/model"',
    )
    arg_par.add_argument(
        "--labels_model",
        "-l",
        default="Theoreticallyhugo/longformer-sep_tok",
        type=str,
        help="model to use for labeling the spans. "
        + "either path to local model or path of huggingface repository "
        + 'in the format of "user/model"',
    )
    arg_par.add_argument(
        "--verbose",
        "-v",
        default=False,
        const=True,
        nargs="?",
        help="set this flag to increase verbosity",
    )
    arg_par.add_argument(
        "--dry",
        "-d",
        default=False,
        const=True,
        nargs="?",
        help="set this flag to run without inference",
    )

    args = arg_par.parse_args()
    return args


# def main():
#     args = full_pipe.get_args()
#     full_pipe.main(
#         args.input_path,
#         args.output_dir,
#         args.spans_model,
#         args.labels_model,
#         args.verbose,
#         args.dry,
#     )
#
# if __name__ == "__main__":
#     main()
