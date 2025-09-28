import serial
import time
import sys

def send_cmd(ser, cmd, delay=0.5):
    ser.write((cmd + "\n").encode())          # gửi lệnh vào UART
    time.sleep(delay)                         # chờ board phản hồi
    out = ser.read_all().decode(errors="ignore")   # đọc toàn bộ output
    print(out, end="")                        # in ra console để debug
    return out

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["rc", "ep"]:
        print("Usage: python set_pcie_mode.py [rc|ep]")
        sys.exit(1)                           # nếu không truyền tham số thì exit

    mode = sys.argv[1]
    port = "COM1"       # có thể đổi sang "/dev/ttyUSB0" tùy OS
    baudrate = 9600

    print(f"Connecting to {port} at {baudrate} baud...")
    ser = serial.Serial(port, baudrate, timeout=1)

    time.sleep(1)          # chờ board sẵn sàng (sau khi reset)
    ser.reset_input_buffer()  # clear buffer cũ

    print(f"Setting PCIe mode to {mode.upper()}...")

    # gửi lệnh vào U-Boot
    send_cmd(ser, f"setenv pcie_mode {mode}")  # set env
    send_cmd(ser, "saveenv")                   # lưu env
    send_cmd(ser, "reset")                     # reset board để boot lại theo env mới

    print("Done. Board rebooting...")

    ser.close()

# lỗi trong code: phải là __name__ và __main__
if __name__ == "__main__":
    main()