"""System information gathering utility."""
import os
import platform
import shutil
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def get_system_info() -> Dict[str, Any]:
    """
    Retrieve system information relevant for Raspberry Pi diagnostics.
    
    Returns:
        Dict containing hostname, python_version, architecture, os, 
        kernel, model, and disk_usage.
    """
    info = {
        "hostname": platform.node(),
        "python_version": platform.python_version(),
        "architecture": platform.machine(),
        "os": platform.system(),
        "kernel": platform.release(),
        "model": "Unknown",
        "disk_usage": "Unknown"
    }
    
    try:
        # Check Raspberry Pi model
        model_file = "/proc/device-tree/model"
        if os.path.exists(model_file):
            with open(model_file, "r") as f:
                info["model"] = f.read().strip('\x00')
    except Exception as e:
        logger.debug("Could not read RPi model: %s", e)
        
    try:
        # Check disk usage of root directory
        total, used, free = shutil.disk_usage("/")
        info["disk_usage"] = {
            "total_gb": round(total / (2**30), 2),
            "used_gb": round(used / (2**30), 2),
            "free_gb": round(free / (2**30), 2)
        }
    except Exception as e:
        logger.debug("Could not read disk usage: %s", e)
        
    return info
