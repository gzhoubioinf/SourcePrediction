# Source prediction

## Getting Started

This package contains a model trained using XGBoost, designed for predicting the host source of E. coli. 
These instructions will help you set up a copy of the project running on your local machine for development and testing purposes

### Prerequisites
	
Before you begin, ensure you have met the following requirements:

- You have a `Windows/Linux/Mac` machine.
- You have installed the latest version of `Python`.
- You have a basic understanding of Python programming.

### Installation

Follow these steps to get your development environment running:

* Clone the repository:

```bash
git clone https://github.com/gzhoubioinf/SourcePrediction.git
```


* Navigate to the project directory:

```bash
cd SourcePrediction
```

* Create a virtual environment:

```bash
python -m venv .venv
```

* Activate virtual environment

```bash
source .venv/bin/activate
```

* Install the required dependencies:

```bash
pip install -r requirements.txt
```

There are two ways to run the Application: the command line and the app.
* Run using the following commmands:

```bash
chmod 777 cmd.py
./cmd.py -i data/genome_sequence_NZ_CP124398.1.txt -o data/test.pdf
```


* Streamlite application. The graphical interface can be run via streamlit. You need to navigate into the streamlit directory and launch the application, usin the following command:

```bash
streamlit run main.py
```

The Streamlit app will start and you can view it in your web browser at http://localhost:8501.

## Usage

We provide a file named 'genome_sequence_NZ_CP124398.1.txt' containing a genome sequence to test the model.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
## License

Distributed under the MIT License. See LICENSE for more information.
