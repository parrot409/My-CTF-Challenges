#docker build . -t asisctf2021_cuuurl
docker run \
	-d \
	--rm \
	--name asisctf2021_cuuurl \
	-p 8000:8000 \
	asisctf2021_cuuurl