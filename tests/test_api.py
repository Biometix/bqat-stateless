from zipfile import ZipFile

from fastapi.testclient import TestClient

from tests import api


### file ###
def test_upload_file_face(tmp_path):
    samples = "tests/samples/file.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*face*.*"))[0]

        response = test.post(
            "/file?modality=face",
            files={"file": open(file, "rb")},
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
        }.issubset(set(resp.keys()))

        assert {
            "file",
            # "image_height",
            # "image_width",
            # "confidence",
            # "bbox_left",
            # "bbox_upper",
            # "bbox_right",
            # "bbox_lower",
            # "smile",
            # "eye_closed_left",
            # "eye_closed_right",
            # "ipd",
            # "pupil_right_x",
            # "pupil_right_y",
            # "pupil_left_x",
            # "pupil_left_y",
            # "yaw_pose",
            # "yaw_degree",
            # "pitch_pose",
            # "pitch_degree",
            # "roll_pose",
            # "roll_degree",
            "quality",
            "background_deviation",
            "background_grayness",
            "blur",
            "blur_face",
            "focus",
            "focus_face",
            "openbr_confidence",
            "openbr_IPD",
            "opencv_face_found",
            "opencv_frontal_face_found",
            "opencv_profile_face_found",
            "opencv_face_height",
            "opencv_face_width",
            "opencv_IPD",
            "opencv_landmarks_count",
            "opencv_eye_count",
            "opencv_mouth_count",
            "opencv_nose_count",
            "over_exposure",
            "over_exposure_face",
            "skin_ratio_face",
            "skin_ratio_full",
        }.issubset(set(resp["results"].keys()))


def test_upload_file_iris(tmp_path):
    samples = "tests/samples/file.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*iris*.*"))[0]

        response = test.post(
            "/file?modality=iris",
            files={"file": open(file, "rb")},
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
        }.issubset(set(resp.keys()))
        assert {
            "quality",
            "contrast",
            "iris_pupil_gs",
            "iris_sclera_gs",
            "iso_greyscale_utilization",
            "iso_iris_pupil_concentricity",
            "iso_iris_pupil_contrast",
            "iso_iris_pupil_ratio",
            "iso_iris_sclera_contrast",
            "iso_margin_adequacy",
            "iso_overall_quality",
            "iso_pupil_boundary_circularity",
            "iso_sharpness",
            "iso_usable_iris_area",
            "normalized_contrast",
            "normalized_iris_diameter",
            "normalized_iris_pupil_gs",
            "normalized_iris_sclera_gs",
            "normalized_iso_greyscale_utilization",
            "normalized_iso_iris_diameter",
            "normalized_iso_iris_pupil_concentricity",
            "normalized_iso_iris_pupil_contrast",
            "normalized_iso_iris_pupil_ratio",
            "normalized_iso_iris_sclera_contrast",
            "normalized_iso_margin_adequacy",
            "normalized_iso_sharpness",
            "normalized_iso_usable_iris_area",
            "normalized_sharpness",
            "pupil_circularity_avg_deviation",
            "sharpness",
            "image_height",
            "image_width",
            "iris_center_x",
            "iris_center_y",
            "iris_diameter",
            "pupil_center_x",
            "pupil_center_y",
            "pupil_diameter",
            "pupil_radius",
        }.issubset(set(resp["results"].keys()))


def test_upload_file_finger(tmp_path):
    samples = "tests/samples/file.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*finger*.*"))[0]

        response = test.post(
            "/file?modality=fingerprint",
            files={"file": open(file, "rb")},
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Width",
            "Height",
            "NFIQ2",
            "Quantized",
            "Resampled",
            "UniformImage",
            "EmptyImageOrContrastTooLow",
            "FingerprintImageWithMinutiae",
            "SufficientFingerprintForeground",
            "EdgeStd",
        }.issubset(set(resp["results"].keys()))


def test_upload_file_speech(tmp_path):
    samples = "tests/samples/file.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*speech*.*"))[0]

        response = test.post(
            "/file?modality=speech",
            files={"file": open(file, "rb")},
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Quality",
            "Noisiness",
            "Discontinuity",
            "Coloration",
            "Loudness",
            "Naturalness",
        }.issubset(set(resp["results"].keys()))


### Base64 ###
def test_upload_base64_face(tmp_path):
    samples = "tests/samples/base64.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*face*base64*.*"))[0]

        response = test.post(
            "/base64?urlsafe=false",
            json={
                "modality": "face",
                "type": "jpg",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            # "image_height",
            # "image_width",
            # "confidence",
            # "bbox_left",
            # "bbox_upper",
            # "bbox_right",
            # "bbox_lower",
            # "smile",
            # "eye_closed_left",
            # "eye_closed_right",
            # "ipd",
            # "pupil_right_x",
            # "pupil_right_y",
            # "pupil_left_x",
            # "pupil_left_y",
            # "yaw_pose",
            # "yaw_degree",
            # "pitch_pose",
            # "pitch_degree",
            # "roll_pose",
            # "roll_degree",
            "quality",
            "background_deviation",
            "background_grayness",
            "blur",
            "blur_face",
            "focus",
            "focus_face",
            "openbr_confidence",
            "openbr_IPD",
            "opencv_face_found",
            "opencv_frontal_face_found",
            "opencv_profile_face_found",
            "opencv_face_height",
            "opencv_face_width",
            "opencv_IPD",
            "opencv_landmarks_count",
            "opencv_eye_count",
            "opencv_mouth_count",
            "opencv_nose_count",
            "over_exposure",
            "over_exposure_face",
            "skin_ratio_face",
            "skin_ratio_full",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64_iris(tmp_path):
    samples = "tests/samples/base64.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*iris*base64*.*"))[0]

        response = test.post(
            "/base64?urlsafe=false",
            json={
                "modality": "iris",
                "type": "bmp",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "quality",
            "contrast",
            "iris_pupil_gs",
            "iris_sclera_gs",
            "iso_greyscale_utilization",
            "iso_iris_pupil_concentricity",
            "iso_iris_pupil_contrast",
            "iso_iris_pupil_ratio",
            "iso_iris_sclera_contrast",
            "iso_margin_adequacy",
            "iso_overall_quality",
            "iso_pupil_boundary_circularity",
            "iso_sharpness",
            "iso_usable_iris_area",
            "normalized_contrast",
            "normalized_iris_diameter",
            "normalized_iris_pupil_gs",
            "normalized_iris_sclera_gs",
            "normalized_iso_greyscale_utilization",
            "normalized_iso_iris_diameter",
            "normalized_iso_iris_pupil_concentricity",
            "normalized_iso_iris_pupil_contrast",
            "normalized_iso_iris_pupil_ratio",
            "normalized_iso_iris_sclera_contrast",
            "normalized_iso_margin_adequacy",
            "normalized_iso_sharpness",
            "normalized_iso_usable_iris_area",
            "normalized_sharpness",
            "pupil_circularity_avg_deviation",
            "sharpness",
            "image_height",
            "image_width",
            "iris_center_x",
            "iris_center_y",
            "iris_diameter",
            "pupil_center_x",
            "pupil_center_y",
            "pupil_diameter",
            "pupil_radius",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64_finger(tmp_path):
    samples = "tests/samples/base64.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*finger*base64*.*"))[0]

        response = test.post(
            "/base64?urlsafe=false",
            json={
                "modality": "fingerprint",
                "type": "png",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Width",
            "Height",
            "NFIQ2",
            "Quantized",
            "Resampled",
            "UniformImage",
            "EmptyImageOrContrastTooLow",
            "FingerprintImageWithMinutiae",
            "SufficientFingerprintForeground",
            "EdgeStd",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64_speech(tmp_path):
    samples = "tests/samples/base64.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*speech*base64*.*"))[0]

        response = test.post(
            "/base64?urlsafe=false",
            json={
                "modality": "speech",
                "type": "wav",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Quality",
            "Noisiness",
            "Discontinuity",
            "Coloration",
            "Loudness",
            "Naturalness",
        }.issubset(set(resp["results"].keys()))


### Base64 urlsafe ###
def test_upload_base64url_face(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*face*base64url*.*"))[0]

        response = test.post(
            "/base64",
            json={
                "modality": "face",
                "type": "jpg",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            # "image_height",
            # "image_width",
            # "confidence",
            # "bbox_left",
            # "bbox_upper",
            # "bbox_right",
            # "bbox_lower",
            # "smile",
            # "eye_closed_left",
            # "eye_closed_right",
            # "ipd",
            # "pupil_right_x",
            # "pupil_right_y",
            # "pupil_left_x",
            # "pupil_left_y",
            # "yaw_pose",
            # "yaw_degree",
            # "pitch_pose",
            # "pitch_degree",
            # "roll_pose",
            # "roll_degree",
            "quality",
            "background_deviation",
            "background_grayness",
            "blur",
            "blur_face",
            "focus",
            "focus_face",
            "openbr_confidence",
            "openbr_IPD",
            "opencv_face_found",
            "opencv_frontal_face_found",
            "opencv_profile_face_found",
            "opencv_face_height",
            "opencv_face_width",
            "opencv_IPD",
            "opencv_landmarks_count",
            "opencv_eye_count",
            "opencv_mouth_count",
            "opencv_nose_count",
            "over_exposure",
            "over_exposure_face",
            "skin_ratio_face",
            "skin_ratio_full",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64url_iris(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*iris*base64url*.*"))[0]

        response = test.post(
            "/base64",
            json={
                "modality": "iris",
                "type": "bmp",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "quality",
            "contrast",
            "iris_pupil_gs",
            "iris_sclera_gs",
            "iso_greyscale_utilization",
            "iso_iris_pupil_concentricity",
            "iso_iris_pupil_contrast",
            "iso_iris_pupil_ratio",
            "iso_iris_sclera_contrast",
            "iso_margin_adequacy",
            "iso_overall_quality",
            "iso_pupil_boundary_circularity",
            "iso_sharpness",
            "iso_usable_iris_area",
            "normalized_contrast",
            "normalized_iris_diameter",
            "normalized_iris_pupil_gs",
            "normalized_iris_sclera_gs",
            "normalized_iso_greyscale_utilization",
            "normalized_iso_iris_diameter",
            "normalized_iso_iris_pupil_concentricity",
            "normalized_iso_iris_pupil_contrast",
            "normalized_iso_iris_pupil_ratio",
            "normalized_iso_iris_sclera_contrast",
            "normalized_iso_margin_adequacy",
            "normalized_iso_sharpness",
            "normalized_iso_usable_iris_area",
            "normalized_sharpness",
            "pupil_circularity_avg_deviation",
            "sharpness",
            "image_height",
            "image_width",
            "iris_center_x",
            "iris_center_y",
            "iris_diameter",
            "pupil_center_x",
            "pupil_center_y",
            "pupil_diameter",
            "pupil_radius",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64url_finger(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*finger*base64url*.*"))[0]

        response = test.post(
            "/base64",
            json={
                "modality": "fingerprint",
                "type": "png",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Width",
            "Height",
            "NFIQ2",
            "Quantized",
            "Resampled",
            "UniformImage",
            "EmptyImageOrContrastTooLow",
            "FingerprintImageWithMinutiae",
            "SufficientFingerprintForeground",
            "EdgeStd",
        }.issubset(set(resp["results"].keys()))


def test_upload_base64url_speech(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    with TestClient(api) as test:
        file = list(tmp_path.glob("**/*speech*base64url*.*"))[0]

        response = test.post(
            "/base64",
            json={
                "modality": "speech",
                "type": "wav",
                "data": file.read_text(),
            },
        )
        print(f"{response.content=}")
        assert response.status_code == 200

        resp = response.json()
        print(f"{resp=}")

        assert {
            "results",
            "engine",
            "modality",
            "id",
            "timestamp",
        }.issubset(set(resp.keys()))
        assert {
            "file",
            "Quality",
            "Noisiness",
            "Discontinuity",
            "Coloration",
            "Loudness",
            "Naturalness",
        }.issubset(set(resp["results"].keys()))
