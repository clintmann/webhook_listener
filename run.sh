echo "Enter RoomID: "
read -s ROOMID
echo "Enter Token: "
read -s TOKEN

export ROOMID
export TOKEN

python main.py
