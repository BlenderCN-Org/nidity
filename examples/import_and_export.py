import nidity


print('import and export example')
nidity.reset()
nidity.files.import_from_sandbox('exported.3ds')
nidity.files.export_to_sandbox('exported')
