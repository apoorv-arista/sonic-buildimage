# BMC Platform Rules
# This file is included when BUILD_SONIC_BMC=y
# It provides minimal image targets without syncd and switching dependencies

# Include image targets based on the base platform
ifeq ($(CONFIGURED_PLATFORM),broadcom)
# Include Arista platform modules for BMC (disabled for ARM64)
#include $(PLATFORM_PATH)/platform-modules-arista.mk
include $(PLATFORM_PATH)/../bmc/one-image-broadcom.mk
include $(PLATFORM_PATH)/../bmc/one-aboot-broadcom.mk
SONIC_ALL += $(SONIC_ONE_IMAGE) $(SONIC_ONE_ABOOT_IMAGE)
endif

# Add other platforms as needed
