#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function.
#       Notice that this function doesn't to return anything because it
#       prints a summary of the results using results_dic and results_stats_dic
#

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(),
          "***")

    print("{:20}: {:3d}".format('N Images: ', results_stats_dic['n_images']))

    print("{:20}: {:3d}".format('N Dog Images: ', results_stats_dic['n_dogs_img']))

    print("{:20}: {:3d}".format('N Not Dog Images: ', results_stats_dic['n_notdogs_img']))

    print("{:20}: {:.2f}%".format('PCT Match: ', results_stats_dic['pct_match']))

    print("{:20}: {:.2f}%".format('PCT Correct Dogs: ', results_stats_dic['pct_correct_dogs']))

    print("{:20}: {:.2f}%".format('PCT Correct Breed: ', results_stats_dic['pct_correct_breed']))

    print("{:20}: {:.2f}%".format('PCT Correct Not Dogs: ', results_stats_dic['pct_correct_notdogs']))

    if (print_incorrect_dogs and (
            (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic[
        'n_images'])
    ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key, values in results_dic.items():
            label, classified, match, is_dog, classified_as_dog = values

            if (match == 0) and ((is_dog + classified_as_dog) == 1):
                print("Real: {:20}    Classifier: {:20}".format(label, classified))

    # IF print_incorrect_breed == True AND there were dogs whose breeds
    # were incorrectly classified - print out these cases
    if (print_incorrect_breed and
            (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])
    ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and
                    results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                                 results_dic[key][1]))
