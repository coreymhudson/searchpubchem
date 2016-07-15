# searchpubchem
Collect PubChem data directly. This tool contains a variety of ways to interact with PubChem. It allows query by Compound ID (NCBI), CAS Number, SMILES and ChemSpider ID. It collects raw XML PubChem output, Substance Data Files (SDFs) and Cross-Reference Links (XREF) and PubChem Fingerprints (CACTVS).

## Comparison with biopython

* See [biopython](https://github.com/biopython/biopython.github.io/)

biopython contains a variety of tools for interacting with NCBI databases. I found, however, that the methods of query were non-exhaustive and that the methods for preprocessessing XML and downloading multiple file-types did not meet my particular goals.

searchpubchem is a tool designed to extract chemical information directly from NCBI's PubChem interface using Python. To that end it is fairly specialized for cheminformatics work.

## Team

[![Corey M. Hudson](https://avatars3.githubusercontent.com/u/6139410?v=3&u=eba4d10795f651f1e665914cde4908af36523267&s=140)](https://github.com/coreymhudson)
|---|
[Corey M. Hudson](https://github.com/coreymhudson)
