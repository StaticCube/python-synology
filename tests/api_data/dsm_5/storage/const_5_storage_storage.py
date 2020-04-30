# -*- coding: utf-8 -*-
"""DSM 5 SYNO.Storage.CGI.Storage data."""
from tests.const import UNIQUE_KEY

DSM_5_STORAGE_STORAGE_DS410J_RAID5_4DISKS_1VOL = {
    "disks": [
        {"id": "test_disk"},
        {
            "container": {
                "order": 0,
                "str": "DS410j",
                "supportPwrBtnDisable": False,
                "type": "internal",
            },
            "device": "/dev/sdd",
            "disable_secera": False,
            "diskType": "SATA",
            "erase_time": 374,
            "firm": "SC60",
            "has_system": True,
            "id": "sdd",
            "is4Kn": False,
            "isSsd": False,
            "is_erasing": False,
            "longName": "Disk 4",
            "model": "ST3000VN007-2E4166      ",
            "name": "Disk 4",
            "num_id": 4,
            "order": 4,
            "portType": "normal",
            "serial": "Z73095S2",
            "size_total": "3000592982016",
            "smart_status": "safe",
            "status": "normal",
            "support": False,
            "temp": 42,
            "used_by": "volume_1",
            "vendor": "Seagate",
        },
        {
            "container": {
                "order": 0,
                "str": "DS410j",
                "supportPwrBtnDisable": False,
                "type": "internal",
            },
            "device": "/dev/sdc",
            "disable_secera": False,
            "diskType": "SATA",
            "erase_time": 410,
            "firm": "80.00A80",
            "has_system": True,
            "id": "sdc",
            "is4Kn": False,
            "isSsd": False,
            "is_erasing": False,
            "longName": "Disk 3",
            "model": "WD30EZRZ-00Z5HB0        ",
            "name": "Disk 3",
            "num_id": 3,
            "order": 3,
            "portType": "normal",
            "serial": "WD-WCC4N0TEJ4F0",
            "size_total": "3000592982016",
            "smart_status": "safe",
            "status": "normal",
            "support": False,
            "temp": 42,
            "used_by": "volume_1",
            "vendor": "WDC     ",
        },
        {
            "container": {
                "order": 0,
                "str": "DS410j",
                "supportPwrBtnDisable": False,
                "type": "internal",
            },
            "device": "/dev/sdb",
            "disable_secera": False,
            "diskType": "SATA",
            "erase_time": 408,
            "firm": "82.00A82",
            "has_system": True,
            "id": "sdb",
            "is4Kn": False,
            "isSsd": False,
            "is_erasing": False,
            "longName": "Disk 2",
            "model": "WD30EFRX-68EUZN0        ",
            "name": "Disk 2",
            "num_id": 2,
            "order": 2,
            "portType": "normal",
            "serial": "WD-WCC4N6LSVCVX",
            "size_total": "3000592982016",
            "smart_status": "safe",
            "status": "normal",
            "support": False,
            "temp": 43,
            "used_by": "volume_1",
            "vendor": "WDC     ",
        },
        {
            "container": {
                "order": 0,
                "str": "DS410j",
                "supportPwrBtnDisable": False,
                "type": "internal",
            },
            "device": "/dev/sda",
            "disable_secera": False,
            "diskType": "SATA",
            "erase_time": 0,
            "firm": "82.00A82",
            "has_system": True,
            "id": "sda",
            "is4Kn": False,
            "isSsd": False,
            "is_erasing": False,
            "longName": "Disk 1",
            "model": "WD30EFRX-68N32N0        ",
            "name": "Disk 1",
            "num_id": 1,
            "order": 1,
            "portType": "normal",
            "serial": "WD-WCC7K5YA5H40",
            "size_total": "3000592982016",
            "smart_status": "90%",
            "status": "normal",
            "support": False,
            "temp": 44,
            "used_by": "volume_1",
            "vendor": "WDC     ",
        },
    ],
    "env": {
        "batchtask": {"max_task": 64, "remain_task": 64},
        "bay_number": "4",
        "ebox": [],
        "fs_acting": False,
        "is_space_actioning": False,
        "isns": {"address": "", "enabled": False},
        "isns_server": "",
        "max_fs_bytes": "17592181850112",
        "max_fs_bytes_high_end": "219902325555200",
        "model_name": "DS410j",
        "ram_enough_for_fs_high_end": False,
        "ram_size": 0,
        "ram_size_required": 32,
        "settingSwap": False,
        "showpooltab": False,
        "status": {"system_crashed": False, "system_need_repair": False},
        "support": {"ebox": False, "raid_cross": False, "sysdef": True},
        "unique_key": UNIQUE_KEY,
    },
    "hotSpares": [],
    "iscsiLuns": [
        {
            "can_do": {
                "data_scrubbing": True,
                "delete": True,
                "expand_by_disk": 1,
                "migrate": {"to_raid5+spare": "1-1", "to_raid6": 1},
            },
            "id": "iscsilun_LUN-1",
            "is_actioning": False,
            "iscsi_lun": {
                "blkNum": "19614744",
                "device_type": "file",
                "lid": 1,
                "location": "volume_1",
                "mapped_targets": [1],
                "name": "LUN-1",
                "restored_time": "0",
                "rootpath": "/volume1",
                "size": "10737418240",
                "thin_provision": False,
                "uuid": "fcf3a450-681c-06cb-fbb9-0400bdbe0780",
                "vaai_extent_size": "0",
                "vaai_support": False,
            },
            "num_id": 1,
            "progress": {"percent": "-1", "step": "none"},
            "status": "normal",
        }
    ],
    "iscsiTargets": [
        {
            "auth": {"mutual_username": "", "type": "none", "username": ""},
            "data_chksum": 0,
            "enabled": True,
            "hdr_chksum": 0,
            "iqn": "iqn.2000-01.com.synology:DiskStation.name",
            "mapped_logical_unit_number": [0],
            "mapped_luns": [1],
            "masking": [
                {"iqn": "iqn.2000-01.com.synology:default.acl", "permission": "rw"}
            ],
            "multi_sessions": False,
            "name": "Target-1",
            "num_id": 1,
            "recv_seg_bytes": 262144,
            "remote": [],
            "send_seg_bytes": 4096,
            "status": "online",
            "tid": 1,
        }
    ],
    "ports": [],
    "storagePools": [],
    "success": True,
    "volumes": [
        {"id": "test_volume"},
        {
            "can_do": {
                "data_scrubbing": True,
                "delete": True,
                "expand_by_disk": 1,
                "migrate": {"to_raid5+spare": "1-1", "to_raid6": 1},
            },
            "container": "internal",
            "device_type": "raid_5",
            "disk_failure_number": 0,
            "disks": ["sda", "sdb", "sdc", "sdd"],
            "eppool_used": "10042748928",
            "fs_type": "ext3",
            "id": "volume_1",
            "is_acting": False,
            "is_actioning": False,
            "is_inode_full": False,
            "is_writable": True,
            "max_fs_size": "17592181850112",
            "maximal_disk_size": "0",
            "minimal_disk_size": "2995767869440",
            "num_id": 1,
            "pool_path": "",
            "progress": {"percent": "-1", "step": "none"},
            "size": {
                "free_inode": "547237217",
                "total": "8846249701376",
                "total_device": "8987275100160",
                "total_inode": "548544512",
                "used": "5719795761152",
            },
            "space_path": "/dev/md2",
            "spares": [],
            "ssd_trim": {"support": "not support"},
            "status": "normal",
            "suggestions": [],
            "timebackup": True,
            "used_by_gluster": False,
            "vol_path": "/volume1",
            "vspace_can_do": {
                "drbd": {
                    "resize": {"can_do": False, "errCode": 53504, "stopService": False,}
                },
                "flashcache": {
                    "apply": {"can_do": False, "errCode": 53504, "stopService": False,},
                    "remove": {
                        "can_do": False,
                        "errCode": 53504,
                        "stopService": False,
                    },
                    "resize": {
                        "can_do": False,
                        "errCode": 53504,
                        "stopService": False,
                    },
                },
                "snapshot": {
                    "resize": {"can_do": True, "errCode": 0, "stopService": False}
                },
            },
        },
    ],
}
