from CLI_1 import main_1

# Run main_1() only when this Python file is executed directly, not when it is imported into another file
# if you run app directly __name__ will equal __main__
# But if this file  imported in another file and be run from it the file.__name__ will equal this file name not __main__
if __name__ == "__main__":
    main_1()