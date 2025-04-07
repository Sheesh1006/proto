services=("backend_service" "chatgpt_service")
mkdir -p ./gen/{backend_service,chatgpt_service}
python_flag() {
  echo --python_out=./gen/$1 --pyi_out=./gen/$1 --grpc_python_out=./gen/$1;
}
for service in ${services[@]}; do
  python -m grpc_tools.protoc -I proto proto/$service/*.proto  $(python_flag $service)
done
