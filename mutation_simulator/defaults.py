from pathlib import Path
from sys import stderr, stdout

from .mut_types import MutType


class Defaults:
	"""Holds default values."""
	OUTBASE = Path(".")

	IGNORE_WARNINGS = False
	QUIET = False

	if stdout.isatty() and stderr.isatty():
		NO_COLOR = False
		NO_PROGRESS = False
	else:
		NO_COLOR = True
		NO_PROGRESS = True

	SPECIES_NAME = "Unknown"
	ASSEMBLY_NAME = "Unknown"
	SAMPLE_NAME = "Unknown"

	TITV = 1

	RATE = 0
	BLOCK = 1
	MINLEN = 1
	MAXLEN = 2
	IV_MINLEN = 2
	IV_MAXLEN = 3

	MUT_BLOCK = {
		MutType.SN: BLOCK,
		MutType.MN: BLOCK,
		MutType.IN: BLOCK,
		MutType.DE: BLOCK,
		MutType.IV: BLOCK,
		MutType.DU: BLOCK,
		MutType.TL: BLOCK,
		MutType.TLI: BLOCK,
	}
