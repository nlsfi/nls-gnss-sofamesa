def outliers(np, pd, tolerance_north_east, tolerance_height, coordinates1, median1, coordinates2, median2, coordinates3, median3, testmeasurements_df):
    northcoordinates_belowtolerances = []
    eastcoordinates_belowtolerances = []
    heights_belowtolerances = []
    abovetolerances = []
    testmeasurements_df_no_outliers = pd.DataFrame()
    testmeasurements_df_outliers = pd.DataFrame()
    i = 0
    while i < len(coordinates1):
        if abs(coordinates1[i] - median1) < tolerance_north_east and abs(coordinates2[i] - median2) < tolerance_north_east and abs(coordinates3[i] - median3) < tolerance_height:
            if testmeasurements_df_no_outliers.empty == True:
                testmeasurements_df_no_outliers = {'Point Number': [testmeasurements_df.loc[i, 'Point Number']],
                                                   'Code': [testmeasurements_df.loc[i, 'Code']],
                                                   'Date': [testmeasurements_df.loc[i, 'Date']],
                                                   'Time': [testmeasurements_df.loc[i, 'Time']],
                                                   'Time Stamp': [testmeasurements_df.loc[i, 'Time Stamp']],
                                                   'Epocs Count': [testmeasurements_df.loc[i, 'Epocs Count']],
                                                   'Solution': [testmeasurements_df.loc[i, 'Solution']],
                                                   'Physical Station ID': [testmeasurements_df.loc[i, 'Physical Station ID']],
                                                   'Virtual Station ID': [testmeasurements_df.loc[i, 'Virtual Station ID']],
                                                   'Northing': [testmeasurements_df.loc[i, 'Northing']],
                                                   'Easting': [testmeasurements_df.loc[i, 'Easting']],
                                                   'Elev': [testmeasurements_df.loc[i, 'Elev']], 
                                                   'Lat': [testmeasurements_df.loc[i, 'Lat']],
                                                   'Lon': [testmeasurements_df.loc[i, 'Lon']],
                                                   'Ell Ht': [testmeasurements_df.loc[i, 'Ell Ht']],
                                                   'Ant Ht': [testmeasurements_df.loc[i, 'Ant Ht']],
                                                   'HRMS': [testmeasurements_df.loc[i, 'HRMS']],
                                                   'VRMS': [testmeasurements_df.loc[i, 'VRMS']],
                                                   'HDOP': [testmeasurements_df.loc[i, 'HDOP']],
                                                   'VDOP': [testmeasurements_df.loc[i, 'VDOP']],
                                                   'PDOP': [testmeasurements_df.loc[i, 'PDOP']],
                                                   'TDOP': [testmeasurements_df.loc[i, 'TDOP']],
                                                   'GDOP': [testmeasurements_df.loc[i, 'GDOP']],                                             
                                                   'GPS': [testmeasurements_df.loc[i, 'GPS']],
                                                   'GLONASS': [testmeasurements_df.loc[i, 'GLONASS']],
                                                   'GALILEO': [testmeasurements_df.loc[i, 'GALILEO']],
                                                   'BEIDOU': [testmeasurements_df.loc[i, 'BEIDOU']],
                                                   'SBAS': [testmeasurements_df.loc[i, 'SBAS']],
                                                   'QZSS': [testmeasurements_df.loc[i, 'QZSS']],
                                                   'Delta N': [testmeasurements_df.loc[i, 'Delta N']],
                                                   'Delta E': [testmeasurements_df.loc[i, 'Delta E']],
                                                   'Delta Elev': [testmeasurements_df.loc[i, 'Delta Elev']],
                                                   'Azimuth': [testmeasurements_df.loc[i, 'Azimuth']],
                                                   'Slant Distance': [testmeasurements_df.loc[i, 'Slant Distance']],
                                                   'Vertical Angle': [testmeasurements_df.loc[i, 'Vertical Angle']],
                                                   'Base Antenna Type': [testmeasurements_df.loc[i, 'Base Antenna Type']],
                                                   'Rover Antenna Type': [testmeasurements_df.loc[i, 'Rover Antenna Type']],
                                                   'dX (mm)': [testmeasurements_df.loc[i, 'dX (mm)']],
                                                   'dY (mm)': [testmeasurements_df.loc[i, 'dY (mm)']],
                                                   'e': [testmeasurements_df.loc[i, 'e']],
                                                   'SigmaX': [testmeasurements_df.loc[i, 'SigmaX']],
                                                   'SigmaY': [testmeasurements_df.loc[i, 'SigmaY']],
                                                   'SigmaZ': [testmeasurements_df.loc[i, 'SigmaZ']],
                                                   'CorXY': [testmeasurements_df.loc[i, 'CorXY']],
                                                   'CorXZ': [testmeasurements_df.loc[i, 'CorXZ']],
                                                   'CorYZ': [testmeasurements_df.loc[i, 'CorYZ']],
                                                   'CovXY': [testmeasurements_df.loc[i, 'CovXY']],
                                                   'CovXZ': [testmeasurements_df.loc[i, 'CovXZ']],
                                                   'CovYZ': [testmeasurements_df.loc[i, 'CovYZ']],
                                                   'Tilt X': [testmeasurements_df.loc[i, 'Tilt X']],
                                                   'Tilt Y': [testmeasurements_df.loc[i, 'Tilt Y']],
                                                   'Heading': [testmeasurements_df.loc[i, 'Heading']],
                                                   'Sigma Tilt X': [testmeasurements_df.loc[i, 'Sigma Tilt X']],
                                                   'Sigma Tilt Y': [testmeasurements_df.loc[i, 'Sigma Tilt Y']],
                                                   'Sigma Heading': [testmeasurements_df.loc[i, 'Sigma Heading']],
                                                   'Magnetic Field': [testmeasurements_df.loc[i, 'Magnetic Field']]}
                testmeasurements_df_no_outliers = pd.DataFrame(data = testmeasurements_df_no_outliers)
                northcoordinates_belowtolerances.append(coordinates1[i])
                eastcoordinates_belowtolerances.append(coordinates2[i])
                heights_belowtolerances.append(coordinates3[i])
            else:
                testmeasurements_df_no_outliers.ix[i] = testmeasurements_df.loc[i, :]
                northcoordinates_belowtolerances.append(coordinates1[i])
                eastcoordinates_belowtolerances.append(coordinates2[i])
                heights_belowtolerances.append(coordinates3[i])
        else:
            if testmeasurements_df_outliers.empty == True:
                testmeasurements_df_outliers = {'Point number': [testmeasurements_df.loc[i, 'Point Number']],
                                                   'Code': [testmeasurements_df.loc[i, 'Code']],
                                                   'Date': [testmeasurements_df.loc[i, 'Date']],
                                                   'Time': [testmeasurements_df.loc[i, 'Time']],
                                                   'Time Stamp': [testmeasurements_df.loc[i, 'Time Stamp']],
                                                   'Epocs Count': [testmeasurements_df.loc[i, 'Epocs Count']],
                                                   'Solution': [testmeasurements_df.loc[i, 'Solution']],
                                                   'Physical Station ID': [testmeasurements_df.loc[i, 'Physical Station ID']],
                                                   'Virtual Station ID': [testmeasurements_df.loc[i, 'Virtual Station ID']],
                                                   'Northing': [testmeasurements_df.loc[i, 'Northing']],
                                                   'Easting': [testmeasurements_df.loc[i, 'Easting']],
                                                   'Elev': [testmeasurements_df.loc[i, 'Elev']], 
                                                   'Lat': [testmeasurements_df.loc[i, 'Lat']],
                                                   'Lon': [testmeasurements_df.loc[i, 'Lon']],
                                                   'Ell Ht': [testmeasurements_df.loc[i, 'Ell Ht']],
                                                   'Ant Ht': [testmeasurements_df.loc[i, 'Ant Ht']],
                                                   'HRMS': [testmeasurements_df.loc[i, 'HRMS']],
                                                   'VRMS': [testmeasurements_df.loc[i, 'VRMS']],
                                                   'HDOP': [testmeasurements_df.loc[i, 'HDOP']],
                                                   'VDOP': [testmeasurements_df.loc[i, 'VDOP']],
                                                   'PDOP': [testmeasurements_df.loc[i, 'PDOP']],
                                                   'TDOP': [testmeasurements_df.loc[i, 'TDOP']],
                                                   'GDOP': [testmeasurements_df.loc[i, 'GDOP']],
                                                   'GPS': [testmeasurements_df.loc[i, 'GPS']],
                                                   'GLONASS': [testmeasurements_df.loc[i, 'GLONASS']],
                                                   'GALILEO': [testmeasurements_df.loc[i, 'GALILEO']],
                                                   'BEIDOU': [testmeasurements_df.loc[i, 'BEIDOU']],
                                                   'SBAS': [testmeasurements_df.loc[i, 'SBAS']],
                                                   'QZSS': [testmeasurements_df.loc[i, 'QZSS']],
                                                   'Delta N': [testmeasurements_df.loc[i, 'Delta N']],
                                                   'Delta E': [testmeasurements_df.loc[i, 'Delta E']],
                                                   'Delta Elev': [testmeasurements_df.loc[i, 'Delta Elev']],
                                                   'Azimuth': [testmeasurements_df.loc[i, 'Azimuth']],
                                                   'Slant Distance': [testmeasurements_df.loc[i, 'Slant Distance']],
                                                   'Vertical Angle': [testmeasurements_df.loc[i, 'Vertical Angle']],
                                                   'Base Antenna Type': [testmeasurements_df.loc[i, 'Base Antenna Type']],
                                                   'Rover Antenna Type': [testmeasurements_df.loc[i, 'Rover Antenna Type']],
                                                   'dX (mm)': [testmeasurements_df.loc[i, 'dX (mm)']],
                                                   'dY (mm)': [testmeasurements_df.loc[i, 'dY (mm)']],
                                                   'e': [testmeasurements_df.loc[i, 'e']],
                                                   'SigmaX': [testmeasurements_df.loc[i, 'SigmaX']],
                                                   'SigmaY': [testmeasurements_df.loc[i, 'SigmaY']],
                                                   'SigmaZ': [testmeasurements_df.loc[i, 'SigmaZ']],
                                                   'CorXY': [testmeasurements_df.loc[i, 'CorXY']],
                                                   'CorXZ': [testmeasurements_df.loc[i, 'CorXZ']],
                                                   'CorYZ': [testmeasurements_df.loc[i, 'CorYZ']],
                                                   'CovXY': [testmeasurements_df.loc[i, 'CovXY']],
                                                   'CovXZ': [testmeasurements_df.loc[i, 'CovXZ']],
                                                   'CovYZ': [testmeasurements_df.loc[i, 'CovYZ']],
                                                   'Tilt X': [testmeasurements_df.loc[i, 'Tilt X']],
                                                   'Tilt Y': [testmeasurements_df.loc[i, 'Tilt Y']],
                                                   'Heading': [testmeasurements_df.loc[i, 'Heading']],
                                                   'Sigma Tilt X': [testmeasurements_df.loc[i, 'Sigma Tilt X']],
                                                   'Sigma Tilt Y': [testmeasurements_df.loc[i, 'Sigma Tilt Y']],
                                                   'Sigma Heading': [testmeasurements_df.loc[i, 'Sigma Heading']],
                                                   'Magnetic Field': [testmeasurements_df.loc[i, 'Magnetic Field']]}
                testmeasurements_df_outliers = pd.DataFrame(data = testmeasurements_df_no_outliers)
                abovetolerances.append([coordinates1[i] - median1, coordinates2[i] - median2, coordinates3[i] - median3])
            else:
                testmeasurements_df_outliers.ix[i] =  testmeasurements_df.loc[i, :]
                abovetolerances.append([coordinates1[i] - median1, coordinates2[i] - median2, coordinates3[i] - median3])
        i += 1
    
    testmeasurements_df_no_outliers = testmeasurements_df_no_outliers.reset_index()
    testmeasurements_df_outliers = testmeasurements_df_outliers.reset_index()
    #print(abovetolerances)
    abovetolerances = np.array(abovetolerances)
    abovetolerances_amount = len(abovetolerances)
    allcoordinates_amount = len(coordinates1)
    abovetolerances_percentage = round((abovetolerances_amount / allcoordinates_amount * 100), 2)
    print('Above tolerances {} measurements of {} measurements. Above tolerances percentage was {} % of all measurements.'.format(abovetolerances_amount, allcoordinates_amount, abovetolerances_percentage))
    return northcoordinates_belowtolerances, eastcoordinates_belowtolerances, heights_belowtolerances, abovetolerances, testmeasurements_df_no_outliers, testmeasurements_df_outliers