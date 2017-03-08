#!/usr/bin/env pyh
import Post
import Search
import GlobalData
import webhoseio


if __name__ == "__main__":
    Test= Search.NextTestCase()
    Test.set_batch(300)
    Test.test_next("Heroin")
