# dry4bash

Use `dry4bash` for DRY verification of Bash projects.

1. Run `dry4bash --help` before first use.
2. Use the project test/build commands that create current coverage or execute the full unit suite.
3. Run the gate with `--fail`.
4. Treat exit `1` as an infrastructure or configuration failure. Do not report it as a quality pass.
5. Treat exit `2` as a quality-gate failure.
