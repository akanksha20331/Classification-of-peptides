Assignment 1 BDMH
Multi-class classification of peptides
Name:- Aman Srivastava (MT20333)
	Akanksha jarwal (MT20331)

Problem Statement:-
To Develop models for peptides having variable length. Amino acids in peptide are represented by a single letter code.Labels are 8 class of peptides with labels A, B, C, D, E, F, G, H..

Libraries used:-
1. Numpy.
2. Pandas.
3. MatPlotLib.pyplot
4. sklearn
5. keras
6. Keras.regulizer l2.

Input:

The code asks 3 user inputs. 
1- Train csv file address.
2- Test csv file address.
3- Sample csv file address.

Text Pre processing :-

Transform the textual data into the numerical form that the machines can process i.e. changing the alphabets into numerical values. 
The code creates a dictionary of considered 20 amino acids with integer values in incremental order to be further used for integer encoding.
One hot encoding method for the same with considering 20 common amino acids as other uncommon amino acids are less in quantity.

Post padding:- 
Post padding is done with max sequence length of 25 which pads with 0 if total sequence length is less than 25 else truncates the sequence up to max length of 25.
P-Feature:
P-feature is used for computing features, in which we compute composition of amino acids and dipeptides, and by that we received X-train and X-test.
Model :-

GridSearchCV:
GridSearchCV implements a “fit” and a “score” method. It also implements “score_samples”, “predict”, “predict_proba”, “decision_function”, “transform” and “inverse_transform” if they are implemented in the estimator used.
The parameters of the estimator is used to apply these methods are optimized by cross-validated grid-search over a parameter grid.
Random Forest Classifier:
A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

Results:-

The model is trained with GridSearchCV, batch_size of 128 and was able to achieve a loss of (0.5620745290892823) with (56.24%) accuracy for validation data.

The test data is then encoded in the desired format and the model predicts the values.
The prediction values are then converted in the form of total 8 class of peptides with labels A, B, C, D, E, F, G, H.  In this 50 fits failed out of a total of 700. The score on these train-test partitions for these parameters will be set to nan.
If these failures are not expected, you can try to debug them by setting error_score='raise'.
Finally the prediction values are saved into a csv file and uploaded to kggle competiton.

Thanks

