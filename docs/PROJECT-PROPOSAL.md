# Handwritten Mathematical Expression Recognition

**CS 59300: Application of Deep Learning – Fall 2026**

**Team:**
- Steven LaGoy – lagosm01@pfw.edu
- Dalton Lybarger – lybads01@pfw.edu
- Pranav Rao – raops01@pfw.edu
- Om Singhal – singo01@pfw.edu

## Project Overview

We propose a deep learning-based application for recognizing handwritten mathematical expressions, including digits, letter variables, and mathematical operations. The intended use case is assisting professors who use digital or virtual whiteboards to convert handwritten mathematical content into LaTeX, a machine-readable format.

The application will allow a user to provide an image of a handwritten mathematical expression, or potentially draw the expression directly within the application. The system will preprocess the input, identify individual handwritten characters, classify those characters using a deep learning model, and reconstruct the characters into a mathematical expression. The resulting expression will be displayed in a digital format including plain text and LaTeX.

## Motivation

Instructors of math or math-adjacent courses frequently use handwritten notation when explaining concepts, particularly on digital or virtual whiteboards. This allows instructors to communicate mathematical ideas naturally; however, the resulting handwriting can be difficult to reuse in digital materials or convert into accessible formats.

Our project will investigate whether deep learning can be used to recognize a defined set of handwritten mathematical characters and reconstruct simple mathematical expressions. Rather than attempting to recognize every possible mathematical symbol or handwritten document, we will establish a manageable vocabulary of characters based on both available datasets and feedback from potential users.

Potential users and stakeholders include professors and faculty in mathematics who use digital whiteboards, computer science faculty who regularly use mathematical notation, and university personnel involved in accessibility or instructional technology.

## Project Scope

The initial version of the application will focus on a predefined set of handwritten mathematical characters. The exact vocabulary will be determined during the requirements-gathering phase, but may include:

- Digits: 0–9
- Common mathematical variables: a, b, c, x, y, z
- Operators: +, −, ×, ÷, =
- Parentheses: ( )
- Basic comparison operators: <, >, ≥, ≤
- Other basic notation such as decimal points and division/fraction notation

These character sets are mostly present in datasets of handwritten ASCII characters. Digits and variables are most accessible from existing datasets.

The project will initially focus on recognizing relatively simple mathematical expressions. More complex notation involving spatial relationships, such as exponents, square roots, fractions, integrals, and summations, will be considered potential extensions rather than requirements for the minimum viable application.

## Deep Learning Approach

We plan to investigate convolutional neural network (CNN) architectures for handwritten character classification. The initial model will be trained to classify individual handwritten characters into the selected vocabulary.

The overall recognition pipeline will consist of:

- Inputting a handwritten mathematical expression.
- Preprocessing the image.
- Detecting or segmenting individual characters.
- Classifying the characters using a CNN-based model.
- Determining the ordering of the recognized characters.
- Reconstructing the mathematical expression.
- Displaying the expression in a machine-readable format.

Existing handwritten-character datasets, including MNIST for handwritten digits, will be investigated as potential sources of training data. Additional datasets or collected samples may be required for alphabetic characters and mathematical symbols.

Data preprocessing may include resizing, grayscale conversion, normalization, thresholding, noise reduction, and data augmentation.

## Model Evaluation

An important component of the project will be evaluating the performance of the deep learning model.

We will investigate how the size and composition of the character vocabulary affects recognition performance and computational requirements. For example, we may compare a model recognizing digits only with models that additionally recognize variables and mathematical operators.

Model performance will be evaluated using metrics such as:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrices

We will also consider computational factors such as training time, inference time, and model size.

In addition to evaluating isolated character classification, we will evaluate the complete application on handwritten expressions to identify errors in character detection, classification, and expression reconstruction.

## User Interface

The final system will be implemented as a user-facing application rather than requiring users to execute code manually. The interface will provide a way to upload or draw a handwritten expression and display the resulting recognized expression.

A possible workflow is:

**Handwritten Input → Recognition → Digital Expression → LaTeX / Accessible Representation**

The interface will be designed to be simple and intuitive so that a user can demonstrate the recognition process without interacting directly with the underlying Python code or model.

## Client and Requirements Gathering

Before finalizing the character vocabulary and application requirements, we plan to consult potential users. In particular, we will seek feedback from mathematics and computer science faculty who use handwritten mathematical notation in their teaching.

We will ask potential users about:

- Their use of virtual or digital whiteboards
- The mathematical notation they commonly write
- How they currently convert handwritten material into digital formats
- Difficulties they encounter when doing so
- Which characters and symbols would be most useful to recognize
- Whether machine-readable output such as LaTeX would be useful in their workflow

We may also consult university accessibility or instructional technology personnel to better understand potential accessibility applications.

This feedback will help us determine an appropriate character vocabulary and prevent the project from becoming unnecessarily broad.

## Project Timeline

With 12 weeks remaining in the semester, we anticipate the following development process:

**Weeks 3–4:** Requirements gathering, potential client interviews, literature/background research, and definition of the initial character vocabulary.

**Weeks 4–5:** Dataset selection or collection and development of the preprocessing pipeline.

**Weeks 5–7:** Development and training of a baseline CNN character classifier.

*Weeks 7–9:* Model experimentation, hyperparameter tuning, and performance evaluation.

*Weeks 8–10:* Character detection/segmentation and reconstruction of simple expressions.

*Weeks 10–13:* Development of the user-facing application and integration with the trained model.

**Weeks 13–14:** End-to-end testing, performance evaluation, and refinement.

**Weeks 14–15:** Final testing, documentation, bug fixes, and preparation for the final demonstration.

## Expected Outcome

At the completion of the project, we expect to have a functional application capable of recognizing a predefined set of handwritten mathematical characters and reconstructing simple mathematical expressions.

The project will provide both a practical demonstration of deep learning for handwritten character recognition and an investigation into the tradeoffs involved in expanding the character vocabulary. The final application will demonstrate the potential of converting handwritten mathematical content into a machine-readable representation that can be more easily reused in digital and accessibility-oriented workflows.
