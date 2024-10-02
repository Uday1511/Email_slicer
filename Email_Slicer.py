# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 18:09:43 2023

@author: Uday
"""

import unittest
import csv

# The EmailProcessor class processes emails from a CSV file and performs various operations on them.


class EmailProcessor:
    def __init__(self, input_file):
        self._input_file = input_file
        self.emails = []  # Public instance attribute

    def _read_emails(self):
        # Reads emails from the CSV input file and populates the 'emails' list.
        try:
            with open(self._input_file, 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip the header row if present
                self.emails = [row[0] for row in reader]
        except FileNotFoundError:
            print("Input file not found.")

    def slice_email(self, email):
        # Slices an email into its username and domain components.
        username, domain = email.split('@')
        return username, domain

    def process_emails(self):
        # Processes each email in the 'emails' list by calling 'slice_email' and returns a list of sliced emails
        sliced_emails_list = []

        for email in self.emails:
            username, domain = self.slice_email(email)
            sliced_emails_list.append([username, domain])

        return sliced_emails_list

    def save_to_csv(self, data, output_file):
        # Saves the provided data to a CSV file with the given output file path.
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Username', 'Domain'])  # Write header
            writer.writerows(data)    # Write data rows

    def process_and_save(self, output_file):
        # Calls the private '_read_emails' method, processes and slices emails, sorts them by domain,
        # and then saves the sorted sliced emails to a CSV output file.
        try:
            self._read_emails()  # Using the private method
            sliced_emails_list = self.process_emails()
            sorted_sliced_emails = sorted(
                sliced_emails_list, key=lambda x: x[1])  # Sort by domain
            self.save_to_csv(sorted_sliced_emails, output_file)
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Email processing and saving completed successfully.")

    def __repr__(self):
        return f"EmailProcessor(input_file={self._input_file})"

    @classmethod
    def example_class_method(cls):
        print("This is an example class method.")


# Unit Tests


class TestEmailProcessor(unittest.TestCase):
    # Unit test for 'process_and_save' method with valid input.
    def test_process_and_save_with_valid_input(self):
        # Test setup: create input and output file paths, and expected email slices.
        self.create_test_input()

# Initialize EmailProcessor and process/save emails.
        email_processor = EmailProcessor(self.input_file)
        email_processor.process_and_save(self.output_file)

# Compare the output with expected results.
        with open(self.output_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            self.assertEqual(header, ['Username', 'Domain'])
            actual_sliced_emails = [row for row in reader]

        self.assertEqual(actual_sliced_emails, self.expected_sliced_emails)
        print("Test for process_and_save with valid input passed.")

# Unit test for 'process_and_save' method with invalid input
    def test_process_and_save_with_invalid_input(self):
        # Create an empty input file
        open(self.input_file, 'w').close()

        email_processor = EmailProcessor(self.input_file)
        email_processor.process_and_save(self.output_file)

        with open(self.output_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, None)
            self.assertIsNone(header)

        print("Test for process_and_save with invalid input passed.")

# Unit test for 'slice_email' method.
    def test_slice_email(self):
        email_processor = EmailProcessor(self.input_file)
        for email, expected_sliced_email in zip(self.emails, self.expected_sliced_emails):
            sliced_email = email_processor.slice_email(email)
            self.assertEqual(sliced_email, tuple(expected_sliced_email))
        print("Test for slice_email passed.")
        # The 'main' function orchestrates the email processing and provides usage examples.


def main():
    # Replace with the actual paths to your CSV input and output files.
    # Replace with the actual path to your CSV file
    input_file = 'C:\\Users\\Uday\\Desktop\\mini study\\CS 521\\uday@bu.edu_Final_project\\input_dataset.csv'

    email_processor = EmailProcessor(input_file)
    email_processor.process_and_save(
        'C:\\Users\\Uday\\Desktop\\mini study\\CS 521\\uday@bu.edu_Final_project\\output_file.csv')

    print("Unique domains:")
    unique_domains_set = set()
    for _, domain in email_processor.process_emails():
        unique_domains_set.add(domain)

    # Using an if conditional to check for a specific domain
    specific_domain = 'harvard.edu'
    if specific_domain in unique_domains_set:
        print(
            f"The domain {specific_domain} is present in the unique domains set.")
    else:
        print(
            f"The domain {specific_domain} is not present in the unique domains set.")


if __name__ == "__main__":
    main()
