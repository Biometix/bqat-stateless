import csv
import json
import math
import random

from bqat.bqat_core.face import scan_face
from bqat.bqat_core.finger import scan_finger
from bqat.bqat_core.iris import scan_iris
from bqat.bqat_core.speech import process_speech


# def test_face_default():
#     """
#     GIVEN a set of mock face images and default engine
#     WHEN the images processed by the module
#     THEN check the output values are within the expected range
#     """
#     with open("tests/conformance/face/tests_default.json") as f:
#         tests = [json.loads(line) for line in f.readlines()]

#     for test in tests:
#         test.pop("_id")
#         test.pop("tag")
#         test.pop("quality")  # optional

#         output = scan_face(test.pop("file"), engine="default")

#         assert isinstance(output, dict)
#         assert output.get("log") == None
#         for k, _ in test.items():
#             assert output[k] == test[k]


# def test_face_biqt():
#     """
#     GIVEN a set of mock face images and alternate engine
#     WHEN the images processed by the module
#     THEN check the output values are within the expected range
#     """
#     with open("tests/conformance/face/tests_biqt.json") as f:
#         tests = [json.loads(line) for line in f.readlines()]

#     for test in tests:
#         test.pop("_id")
#         test.pop("tag")

#         output = scan_face(test.pop("file"), engine="biqt")

#         assert isinstance(output, dict)
#         assert output.get("log") == None
#         for k, _ in test.items():
#             assert output[k] == test[k]


# def test_finger_nfiq2():
#     """
#     GIVEN the nfiq2 conformance dataset
#     WHEN the images processed by the module
#     THEN check if the output values conform
#     """
#     # Case 1
#     with open("tests/conformance/finger/expected.csv") as f:
#         tests = list(csv.DictReader(f))
#         tests = random.sample(tests, 10)

#     for test in tests:
#         file = "tests/conformance/finger/images/" + test["Filename"]

#         output = scan_finger(file)

#         assert isinstance(output, dict)
#         if output.get("log"):
#             assert output["log"]["nfiq2"] == test["OptionalError"]
#         else:
#             assert output["NFIQ2"] == test["QualityScore"]


# def test_iris_normal():
#     """
#     GIVEN a set of mock iris images
#     WHEN the images processed by the module
#     THEN check the output values are within the expected range
#     """
#     # Case 1
#     with open("tests/conformance/iris/tests.json") as f:
#         tests = [json.loads(line) for line in f.readlines()]

#     for test in tests:
#         test.pop("_id")
#         test.pop("tag")

#         output = scan_iris(test.pop("file"))

#         assert isinstance(output, dict)
#         assert output.get("log") == None
#         for k, _ in test.items():
#             assert output[k] == test[k]


# def test_speech_normal():
#     """
#     GIVEN a set of mock speech samples
#     WHEN the samples processed by the module
#     THEN check the output values are within the expected range
#     """
#     # Case 1
#     with open("tests/conformance/speech/tests.json") as f:
#         tests = [json.loads(line) for line in f.readlines()]

#     for test in tests:
#         test.pop("_id")
#         test.pop("tag")

#         output = process_speech(test.pop("file"), "file")

#         assert isinstance(output, dict)
#         assert output.get("log") == None
#         for k, _ in test.items():
#             assert math.isclose(float(output[k]), float(test[k]), abs_tol=0.001)
