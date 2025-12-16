# phy-credo is only available for amd64 architecture
ifeq ($(CONFIGURED_ARCH),amd64)
PHY_CREDO = phy-credo_1.0_amd64.deb
$(PHY_CREDO)_URL = "https://github.com/aristanetworks/sonic-firmware/raw/24716c4e03f223d8e18afff786ac427f6ac77fe0/phy/phy-credo_1.0_amd64.deb"
SONIC_ONLINE_DEBS += $(PHY_CREDO)
endif
