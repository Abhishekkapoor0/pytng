import pytng

import numpy as np
import pytest


def test_load_bad_file(TNG_BAD_FILEPATH):
    with pytest.raises(IOError):
        with pytng.TNGFile(TNG_BAD_FILEPATH) as tng:
            tng.read()

def test_len(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        assert TNG_REF_DATA.length == tng.n_frames
        assert TNG_REF_DATA.length == len(tng)

def test_iter(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        for i, ts in enumerate(tng):
            assert i == ts.step

def test_natoms(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        assert TNG_REF_DATA.natoms == tng.n_atoms


def test_first_positions(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        first_frame = tng.read().xyz
        assert np.array_equal(TNG_REF_DATA.first_frame, first_frame)


def test_last_positions(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        tng.seek(tng.n_frames - 1)
        last_frame = tng.read().xyz
        assert np.array_equal(TNG_REF_DATA.last_frame, last_frame)

def test_time(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        tng.seek(tng.n_frames - 1)
        time = tng.read().time
        assert np.array_equal(TNG_REF_DATA.last_frame_time, time)


def test_box(TNG_REF_DATA, TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        frame = tng.read()
        assert np.array_equal(TNG_REF_DATA.box, frame.box)

def test_box(TNG_REF_FILEPATH):
    with pytng.TNGFile(TNG_REF_FILEPATH) as tng:
        for i, frame in enumerate(tng):
            assert i == frame.step

        for i, frame in enumerate(tng):
            assert i == frame.step


def test_path(TNG_REF_FILEPATH):
    assert isinstance(TNG_REF_FILEPATH, str)
