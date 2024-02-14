import time
from zipfile import ZipFile

import anyio
import pytest
from httpx import AsyncClient

from tests import api

STRESS = 100


### Base64 urlsafe ###
@pytest.mark.anyio
async def test_upload_base64url_face(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    async with AsyncClient(app=api, base_url="http://localhost:8848") as test:
        file = list(tmp_path.glob("**/*face*base64url*.*"))[0]

        print(f"started: {time.ctime()}")
        count = 0
        for _ in range(STRESS):
            response = await test.post(
                "/base64",
                json={
                    "modality": "face",
                    "type": "jpg",
                    "data": file.read_text(),
                },
            )
            # print(f"{response.content=}")
            assert response.status_code == 200
            count += 1

            resp = response.json()
            # print(f"{resp=}")

            assert {
                "results",
                "engine",
                "modality",
                "id",
                "timestamp",
            }.issubset(set(resp.keys()))

    assert count == STRESS
    print(f"{count} requests made: {time.ctime()}")


@pytest.mark.anyio
async def test_upload_base64url_iris(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    async with AsyncClient(app=api, base_url="http://localhost:8848") as test:
        file = list(tmp_path.glob("**/*iris*base64url*.*"))[0]

        print(f"started: {time.ctime()}")
        count = 0
        for _ in range(STRESS):
            response = await test.post(
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

    assert count == STRESS
    print(f"{count} requests made: {time.ctime()}")


@pytest.mark.anyio
async def test_upload_base64url_finger(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    async with AsyncClient(app=api, base_url="http://localhost:8848") as test:
        file = list(tmp_path.glob("**/*finger*base64url*.*"))[0]

        print(f"started: {time.ctime()}")
        count = 0
        for _ in range(STRESS):
            response = await test.post(
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

    assert count == STRESS
    print(f"{count} requests made: {time.ctime()}")


@pytest.mark.anyio
async def test_upload_base64url_speech(tmp_path):
    samples = "tests/samples/base64url.zip"
    with ZipFile(samples, "r") as z:
        z.extractall(tmp_path)

    async with AsyncClient(app=api, base_url="http://localhost:8848") as test:
        file = list(tmp_path.glob("**/*speech*base64url*.*"))[0]

        print(f"started: {time.ctime()}")
        count = 0
        for _ in range(STRESS):
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

    assert count == STRESS
    print(f"{count} requests made: {time.ctime()}")
