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
                                                   'Solution': [testmeasurements_df.loc[i, 'Solution']],
                                                   'Physical Station ID': [testmeasurements_df.loc[i, 'Physical Station ID']],
                                                   'Virtual Station ID': [testmeasurements_df.loc[i, 'Virtual Station ID']],
                                                   'Northing': [testmeasurements_df.loc[i, 'Northing']],
                                                   'Easting': [testmeasurements_df.loc[i, 'Easting']],
                                                   'Elev': [testmeasurements_df.loc[i, 'Elev']], 
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
                                                   'QZSS': [testmeasurements_df.loc[i, 'QZSS']]}
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
                testmeasurements_df_outliers = {'Point Number': [testmeasurements_df.loc[i, 'Point Number']],
                                                   'Code': [testmeasurements_df.loc[i, 'Code']],
                                                   'Date': [testmeasurements_df.loc[i, 'Date']],
                                                   'Time': [testmeasurements_df.loc[i, 'Time']],
                                                   'Solution': [testmeasurements_df.loc[i, 'Solution']],
                                                   'Physical Station ID': [testmeasurements_df.loc[i, 'Physical Station ID']],
                                                   'Virtual Station ID': [testmeasurements_df.loc[i, 'Virtual Station ID']],
                                                   'Northing': [testmeasurements_df.loc[i, 'Northing']],
                                                   'Easting': [testmeasurements_df.loc[i, 'Easting']],
                                                   'Elev': [testmeasurements_df.loc[i, 'Elev']], 
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
                                                   'QZSS': [testmeasurements_df.loc[i, 'QZSS']]}
                testmeasurements_df_outliers = pd.DataFrame(data = testmeasurements_df_no_outliers)
                abovetolerances.append([coordinates1[i] - median1, coordinates2[i] - median2, coordinates3[i] - median3])
            else:
                testmeasurements_df_outliers.ix[i] =  testmeasurements_df.loc[i, :]
                abovetolerances.append([coordinates1[i] - median1, coordinates2[i] - median2, coordinates3[i] - median3])
        i += 1
        
    # TR 
    if testmeasurements_df_no_outliers.empty == True:
        print('All points above set tolerance values!')
        testmeasurements_df_no_outliers = {'Point Number': [None],
                                                   'Code': [None],
                                                   'Date': [None],
                                                   'Time': [None],
                                                   'Solution': [None],
                                                   'Physical Station ID': [None],
                                                   'Virtual Station ID': [None],
                                                   'Northing': [None],
                                                   'Easting': [None],
                                                   'Elev': [None], 
                                                   'Ell Ht': [None],
                                                   'Ant Ht': [None],
                                                   'HRMS': [None],
                                                   'VRMS': [None],
                                                   'HDOP': [None],
                                                   'VDOP': [None],
                                                   'PDOP': [None],
                                                   'TDOP': [None],
                                                   'GDOP': [None],                                             
                                                   'GPS': [None],
                                                   'GLONASS': [None],
                                                   'GALILEO': [None],
                                                   'BEIDOU': [None],
                                                   'SBAS': [None],
                                                   'QZSS': [None]}
        testmeasurements_df_no_outliers = pd.DataFrame(data = testmeasurements_df_no_outliers)
        
    testmeasurements_df_no_outliers = testmeasurements_df_no_outliers.reset_index()
    testmeasurements_df_outliers = testmeasurements_df_outliers.reset_index()
    abovetolerances = np.array(abovetolerances)
    abovetolerances_amount = len(abovetolerances)
    allcoordinates_amount = len(coordinates1)
    abovetolerances_percentage = round((abovetolerances_amount / allcoordinates_amount * 100), 2)
    # print('Above tolerances {} measurements of {} measurements. Above tolerances percentage was {} % of all measurements.'.format(abovetolerances_amount, allcoordinates_amount, abovetolerances_percentage))
    abovetolerances_text = 'Above tolerances {} measurements of {} measurements. Above tolerances percentage was {} % of all measurements.'.format(abovetolerances_amount, allcoordinates_amount, abovetolerances_percentage)
    return northcoordinates_belowtolerances, eastcoordinates_belowtolerances, heights_belowtolerances, abovetolerances, testmeasurements_df_no_outliers, testmeasurements_df_outliers, abovetolerances_text, allcoordinates_amount, abovetolerances_amount, abovetolerances_percentage