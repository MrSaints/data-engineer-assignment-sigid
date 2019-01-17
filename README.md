# Data Engineer Assignment - SIGID

**This assignment should take approximately 3 hours.**


## Introduction

✍️ You are a data engineer at a team that is responsible for researching techniques for verifying, and identifying handwritten signatures.

The team is currently receiving signatures in the form of images through a production, online digital signature service (no verification or identification is currently carried out), and through datasets collected offline (e.g. scanned, and cropped from hard-copy documents).

To ensure a simple, but coherent research, and development environment, the team lead proposed consolidating the storage, and access of the datasets (i.e. a data warehouse) instead of having them in disparate sources / several different data lakes.

An initial design in Python for structuring the data, and for the read / write interfaces has already been put in place by the team lead based on some recurring themes / patterns in the data so far - see `sigid` directory. We have also downloaded the datasets into the `datasets` directory.

Thus, your task is to **write a working ETL script / program in Python using as much of the initial design as possible**.

You can find an example of how the initial design should be used in `sigid/example.py`. You can also test run it using: `python -m sigid.example`. The initial design relies on mock data stores (aka repositories).

**The initial design CAN be changed where you deem appropriate, and we do encourage this, but any changes SHOULD be documented.**


## Our Expectations

We are NOT looking for a "perfect" solution. Please try to get a fully working assignment. Focus on simplicity, and making it work, before making it right, and making it fast.

The assignment is looking out for your ability:

- To cope with other people's documentation, abstractions, and code
- To work with unfamiliar technologies
- To work with imperfect information
- To understand, and handle semi-structured raw data
- To identify, and handle risks / edge-cases
- To account for potential changes in requirements
- To communicate your thought process, and solution
- To evaluate your work, and other people's work

If you are familiar with Docker, we have added a base image (`Dockerfile`) for your development convenience. If you are not familiar with Docker, you can disregard it, we do not expect you to be familiar with it.


## What Is Required

You can structure the assignment however you want. But, for your convenience, we have provided a base Jupyter notebook you can work from (`Assignment.ipynb`), and submit to us. We ask that the following is completed before submission:

- [ ] An executable ETL script / program in Python to load data from `datasets/SOURCE_A` to the data warehouse using the `register_signatures` interface (see `sigid/example.py`)
- [ ] Automated tests
    - [ ] Can the script / program correctly extract data?
    - [ ] Can the script / program correctly transform data?
    - [ ] Can the script / program handle edge-cases?
- [ ] Documentation
    - [ ] What is needed to run the script / program?
    - [ ] How can we run the script / program?
    - [ ] Evaluation (e.g. what difficulties did you encounter? what assumptions were made? what improvements can be made?)

**NOTE:** documentation for the datasets can be found within the dataset directory. See `datasets/SOURCE_A/README.md` for example.


### Stretch Goals (Optional)

- [ ] Ensure typechecks passes (run `./dev/typecheck.sh`)
- [ ] Implement _idempotence_ in the ETL process
- [ ] Containerise the script / program for easy execution using Docker, and include instructions
- [ ] A similar ETL script / program for `datasets/SOURCE_B`
- [ ] Implement a signee and/or a signature data store using a relational database (e.g. MySQL, Postgresql, etc)


## What Is NOT Required

**Please DO NOT work on following as it is NOT required for this assignment:**

- Any complex architecture (e.g. Airflow, Luigi, etc)
- Any sort of web API
- Feature extraction or selection
- Implementation of signature verification or identification algorithms
- Implementation of an asset service (use the mock)


## Submission

Please ZIP the entire assignment before submission.

If you a familiar with code formatting, run `./dev/format.sh`, otherwise you can disregard this step.
