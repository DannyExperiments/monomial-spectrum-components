# Reproduce version 1.0.0

Run the standard-library checks from the root.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The checks validate the tracked inventory and checksums and replay the worked proof illustrations. Open the standalone explorer directly in a browser. [Manuscript build](paper/BUILD.md)

Run `python3 formal/closing/verify.py` with the versions pinned in `formal/closing/` to replay the partial Lean proof. [Declarations and scope](formal/closing/README.md)
