# -*- coding: utf-8 -*-
"""DSM 5 SYNO.Core.System.Utilization data."""

DSM_5_CORE_UTILIZATION = {
    "data": {
        "cpu": {
            "15min_load": 53,
            "1min_load": 57,
            "5min_load": 56,
            "device": "System",
            "other_load": 63,
            "system_load": 10,
            "user_load": 27,
        },
        "disk": {
            "disk": [
                {
                    "device": "sda",
                    "display_name": "Disk 1",
                    "read_access": 21,
                    "read_byte": 645529,
                    "type": "internal",
                    "utilization": 46,
                    "write_access": 4,
                    "write_byte": 86220,
                },
                {
                    "device": "sdb",
                    "display_name": "Disk 2",
                    "read_access": 23,
                    "read_byte": 711338,
                    "type": "internal",
                    "utilization": 33,
                    "write_access": 4,
                    "write_byte": 95641,
                },
                {
                    "device": "sdc",
                    "display_name": "Disk 3",
                    "read_access": 21,
                    "read_byte": 786841,
                    "type": "internal",
                    "utilization": 31,
                    "write_access": 5,
                    "write_byte": 99874,
                },
                {
                    "device": "sdd",
                    "display_name": "Disk 4",
                    "read_access": 21,
                    "read_byte": 729907,
                    "type": "internal",
                    "utilization": 32,
                    "write_access": 4,
                    "write_byte": 76663,
                },
                {
                    "device": "sdq",
                    "display_name": "USB Disk 1",
                    "read_access": 0,
                    "read_byte": 0,
                    "type": "usb",
                    "utilization": 0,
                    "write_access": 0,
                    "write_byte": 0,
                },
            ],
            "total": {
                "device": "total",
                "read_access": 86,
                "read_byte": 2873615,
                "utilization": 28,
                "write_access": 17,
                "write_byte": 358398,
            },
        },
        "memory": {
            "avail_real": 8188,
            "avail_swap": 1933436,
            "buffer": 3700,
            "cached": 25636,
            "device": "Memory",
            "memory_size": 131072,
            "real_usage": 68,
            "si_disk": 5,
            "so_disk": 3,
            "swap_usage": 7,
            "total_real": 118464,
            "total_swap": 2097080,
        },
        "network": [
            {"device": "total", "rx": 1680, "tx": 553},
            {"device": "eth0", "rx": 1680, "tx": 553},
        ],
        "space": {
            "lun": [],
            "total": {
                "device": "total",
                "read_access": 261,
                "read_byte": 1069875,
                "utilization": 100,
                "write_access": 51,
                "write_byte": 208896,
            },
            "volume": [
                {
                    "device": "md2",
                    "display_name": "volume1",
                    "read_access": 261,
                    "read_byte": 1069875,
                    "utilization": 100,
                    "write_access": 51,
                    "write_byte": 208896,
                }
            ],
        },
        "time": 1586592505,
    },
    "success": True,
}
