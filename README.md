# Arabic Fake News Detection using Deep Learning

![Project Logo](./images/logo.png)

## Description
This project aims to help users detect Arabic fake news in various forms such as articles, tweets, and statements using deep learning and natural language processing (NLP). The project provides a user-friendly Google Chrome extension interface that leverages the power of the Arabert model from Hugging Face.

## Inspiration
The challenging nature of the Arabic language and the scarcity of Arabic fake news datasets motivated us to create a reliable solution for Arabic fake news detection. We recognized the importance of addressing misinformation in Arabic and wanted to develop a tool specifically tailored for accurate detection of fake news in this language.

## Features
- User-friendly interface as a Google Chrome extension
- Utilizes the Arabert model[1] from Hugging Face for accurate Arabic text processing

## Technologies Used
- Python: for the core functionality and implementation of the fake news detection algorithm
- Node.js: for building the Chrome extension and creating the user interface

## Prerequisites
Before using the project, make sure the following dependencies are installed:
- Transformers: `pip install transformers`
- Arabert: `pip install arabert`
- Flask: `pip install flask`
- Torch: `pip install torch`

## Installation and Usage
1. Download the project code files from the repository.
2. Install a Chromium-based browser (e.g., Google Chrome, Microsoft Edge).
3. Open the browser and go to the extensions or add-ons page.
4. Enable 'Developer Mode' in the browser's extensions settings.
5. Load the project's code files as an unpacked extension.
6. Open a terminal or command prompt, navigate to the project directory, and run `app.py` to start the local server.
7. Access the extension by clicking on its icon in the browser's toolbar.

## Future Plans and Enhancements
- Publishing the extension on the Google Store for easy installation and wider accessibility.
- Increasing compatibility with multiple browsers beyond Chromium-based ones.
- Expanding supported languages for broader fake news detection coverage.
- Exploring more deep learning and NLP techniques to improve accuracy.

## Contributions
We welcome contributions to our project! Here's how you can contribute:
- Use the Arabic Fake News Detection extension and kindly mention it when sharing or discussing it with others.
- Report issues and suggest improvements by opening an issue on the project's repository.
- Contribute code or documentation improvements by submitting a pull request.

## Testing
We have tested our project using unseen test data from the Arabic Fake News Dataset (AFND) [2], as well as various real and fake articles and tweets from the internet. This testing allowed us to evaluate the performance and accuracy of our project. You can use the provided test scripts or test cases to verify the functionality of the Arabic Fake News Detection system.

## Acknowledgments
We would like to acknowledge and express our gratitude to the authors of the Arabic Fake News Dataset (AFND) [2] and AUBmindLabs for AraBERT MODEL[1]. Their products played a vital role in developing, completing and evaluating our Arabic Fake News Detection system.

[1] AraBERT Model:[Link to model on HuggingFace](https://huggingface.co/aubmindlab/bert-base-arabertv2?text=%D8%B9%D8%A7%D8%B5%D9%85+%2B%D8%A9+%D9%85%D8%B5%D8%B1+%D9%87%D9%8A+%5BMASK%5D+.)

[2] Arabic Fake News Dataset (AFND): [Link to the dataset](https://www.sciencedirect.com/science/article/pii/S2352340922003493)

## Contact
If you have any questions, feedback, or suggestions, please reach out to us through GitHub Issues or Discussions.

We value your contribution and appreciate your support in combating fake news in Arabic!

Feel free to customize and modify the above template as per your specific project requirements.
