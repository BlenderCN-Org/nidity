import nidity


print('import and export example')
nidity.reset()
nidity.files.import_from_sandbox('exported.dae')
nidity.files.export_to_sandbox('exported.dae')
