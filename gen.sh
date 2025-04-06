services=("backend_service" "chatgpt_service")
mkdir gen
for service in ${services[@]}; do
  mkdir gen/$service
  touch gen/$service/setup.py
  mkdir gen/$service/$service
  touch gen/$service/$service/__init__.py
  proto="${service}.proto"
  python -m grpc_tools.protoc \
  --python_out=gen/$service/$service \
  --grpc_python_out=gen/$service/$service \
  --pyi_out=gen/$service/$service \
  -I=proto/$service $proto
done
