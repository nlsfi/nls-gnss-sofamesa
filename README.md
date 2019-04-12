# NLS GNSS SOFAMESA

### GNSS Measurement Accuracy Analysis Software of the National Land Survey of Finland
*Author: Tuukka Mattila. Don't hesitate to contact via LinkedIn:* [LinkedIn profile](https://www.linkedin.com/in/tuukkamattila/)

*Thank you for the help: Topi Rikkinen, Marko Ollikainen, Antti Laaksonen, Hannu Koivula, and Ari Huvinen*

**Capabilities**

*  Watch [a video of the National Land Survey of Finland](https://www.youtube.com/watch?v=urj7mGjKY9Q)
*  Import your own [GNSS measurements file (.csv)](test_measurements_example.csv)
*  Import your own [GNSS reference points coordinates file (.csv)](reference_points_example.csv)
*  Set your own tolerance values for horizontal and vertical outlier recognition
*  Visual outlier recognition based on the Kernel Density Estimator (KDE) plots of the distributions of errors
*  Calculate the means, medians and standard deviations of the North and East coordinates and Heights
*  The GNSS measurement data can be fitted to follow the Gaussian distribution. You can produce Gaussian distribution models with the help of the means and standard deviations of the GNSS measurements. Utilize random number generation to produce the models and calculate distributions. You can test the models with varying sample sizes.
*  Calculate inner accuracies (precisions)
*  Calculate outer accuracies (accuracies)
*  (IN PROGRESS) Produce a [Measurement report](Measurement_Report.pdf) .pdf file of the figures and statistics of the GNSS measurements.

**Analysis of**

*  The Number of Satellites (GPS, GLONASS, GALILEO, BEIDOU)
*  The DOP Values: HDOP, VDOP, PDOP, TDOP, GDOP
*  The Reported HRMS and VRMS Values of the Receiver
*  The outlier recognition
*  The means, medians and standard deviations of the North and East coordinates and Heights
*  The inner accuracies (precisions): Horizontal RMSE and 2dRMSE, Vertical RMSE and 2dRMSE, North precisions, East precisions, Vertical precisions, Horizontal precisions, Horizontal precisions with DOP values, 3D precisions with DOP values, Vertical precisions with DOP values
*  (IN PROGRESS) The outer accuracies (accuracies): Horizontal RMSE and 2dRMSE, Vertical RMSE and 2dRMSE, North accuracies, East accuracies, Vertical accuracies, Horizontal accuracies
*  The Time Spent (s) of the Program  

**[Output figures](Figures.zip)**

*  A_The Number of Satellites (No Outliers or Float Solutions Removed)
*  B_The DOP Values (No Outliers or Float Solutions Removed)
*  C_The Reported HRMS and VRMS Values of the Receiver  (No Outliers or Float Solutions Removed)
*  D_KDE Plot for Outlier Recognition (PRECISION, INNER ACCURACY)
*  E_KDE Plot for the Distribution of Errors (PRECISION, INNER ACCURACY)
*  F_Gaussian Distribution Models for the Distributions of Errors (PRECISION, INNER ACCURACY)
*  G_The PRECISION of the point (INNER accuracy) (m) HORIZONTAL
*  H_The PRECISION of the point (INNER accuracy) (m) NORTH
*  I_The PRECISION of the point (INNER accuracy) (m) EAST
*  J_The PRECISION of the point (INNER accuracy) (m) VERTICAL
*  K_The ACCURACY of the point (OUTER accuracy) (m) HORIZONTAL
*  L_The ACCURACY of the point (OUTER accuracy) (m) NORTH
*  M_The ACCURACY of the point (OUTER accuracy) (m) EAST
*  N_The ACCURACY of the point (OUTER accuracy) (m) VERTICAL
*  O_The Horizontal PRECISION of the point (INNER accuracy) (m) with DOP values
*  P_The 3D PRECISION of the point (INNER accuracy) (m) with DOP values.png
*  Q_The Vertical PRECISION of the point (INNER accuracy) (m) with DOP values

**Requirements:**

*  Windows Operating System
*  Free access through firewall
*  The test data should consist of at least 3600 measurements per reference point. Is the requirement met? For example, with 10 seconds measurement time and 1 second epocs, averaged solutions should be 3600 pcs. Does the file consist of at least 3600 measurements for the point?
*  Import the [GNSS measurement data as .csv file](test_measurements_example.csv) and separated with "," and formatted as (the order of the columns doesn't matter) Point Number,Code,Date,Time,Time Stamp,Epocs Count,Solution,Physical Station ID,Virtual Station ID,Northing,Easting,Elev,Lat,Lon,Ell Ht,Ant Ht,HRMS,VRMS,HDOP,VDOP,PDOP,GDOP,TDOP,GPS,GLONASS,GALILEO,BEIDOU,SBAS,QZSS,Delta N,Delta E,Delta Elev,Azimuth,Slant Distance,Vertical Angle,Base Antenna Type,Rover Antenna Type,dX (mm),dY (mm),e,SigmaX,SigmaY,SigmaZ,CorXY,CorXZ,CorYZ,CovXY,CovXZ,CovYZ,Tilt X,Tilt Y,Heading,Sigma Tilt X,Sigma Tilt Y,Sigma Heading,Magnetic Field].
*  Import the [GNSS reference points coordinates data as .csv file](reference_points_example.csv) and formatted as (the order of the columns doesn't matter) [Reference Point Number,Northing,Easting,Elevation].

## INSTRUCTIONS

*In order to successfully operate the NLS GNSS SOFAMESA, please follow the instructions below.*

### Phases

1.  Download all of the files provided as a .zip file
2.  Unzip the files to a proper location
3.  Install Anaconda Platform for Windows: https://www.anaconda.com/
4.  Make sure that your firewall doesn't block any of the operations related to the Anaconda platform
5.  (IN PROGRESS) Install the required libraries, if not defaultly installed:
*   iPython
*   time
*   numpy
*   matplotlib
*   pandas
*   seaborn
*   os
*   sys
*   math
*   pathlib
*   glob
*   re
*   string
*   datetime
*   reportlab
6.  Launch Anaconda Prompt
7.  Change the directory to the folder, where the [NLS_GNSS_SOFAMESA.ipynb](NLS_GNSS_SOFAMESA.ipynb) file is located. In Anaconda Prompt, write: *cd [the path here without the brackets]*
8.  Launch Jupyter Notebook. In Anaconda Prompt, write: *jupyter-notebook*
9.  When the browser is launched, select the proper .ipynb file from the directory view
10. Run the notebook cell by cell or restart the current kernel and re-run the whole notebook
11. The figures will be created to a new "figures" subfolder in your .ipynb folder location
12. (IN PROGRESS) The [Measurement_report.pdf](Measurement_Report.pdf) file will be created to your [NLS_GNSS_SOFAMESA.ipynb](NLS_GNSS_SOFAMESA.ipynb) file folder location
--------------------------------------------------------------------------------

*Honours:*

>  "...one guy’s noise is the other guy’s signal..." - [Martin Vermeer, Professor of Geodesy, Department of the Built Environment, School of Engineering, Aalto University](https://users.aalto.fi/~mvermeer/) [28th March 2019, Page 115, Methods of Navigation](https://users.aalto.fi/~mvermeer/nav-en.pdf) 

>  "What you see from where you are" not "Where you are from what you see" - Greg Welch & Gary Bishop [28th March 2019, Page 15, An Introduction to the Kalman Filter](http://www.cs.unc.edu/~tracker/media/pdf/SIGGRAPH2001_Slides_08.pdf)

>  "...Like a coffee filter filters coffee from coffee-grounds, the Kalman filter filters the signal (the state vector) from the noise of both the observation and the movement process..." - [Martin Vermeer, Professor of Geodesy, Department of the Built Environment, School of Engineering, Aalto University](https://users.aalto.fi/~mvermeer/) [28th March 2019, Page 31, Methods of Navigation](https://users.aalto.fi/~mvermeer/nav-en.pdf) 

>  "If you don't know, then you can't know" -TR [28th March 2019]
