
build:
	# echo "building package"
	python setup.py sdist bdist_wheel

publish:
	# echo "publishing package to pypi index"
    twine upload --repositry pypi dist/*