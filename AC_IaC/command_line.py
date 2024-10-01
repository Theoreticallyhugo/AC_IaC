from .inference import full_pipe

def main():
    args = full_pipe.get_args()
    full_pipe.main(
        args.input_path,
        args.output_dir,
        args.spans_model,
        args.labels_model,
        args.verbose,
        args.dry,
    )

if __name__ == "__main__":
    main()
