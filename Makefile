#############################################################################
# Makefile for building: pyqt
# Generated by qmake (2.01a) (Qt 4.8.0) on: ?? 6? 26 14:58:27 2012
# Project:  pyqt.pro
# Template: subdirs
# Command: /opt/QtSDK/Desktop/Qt/4.8.0/gcc/bin/qmake -o Makefile pyqt.pro
#############################################################################

first: make_default
MAKEFILE      = Makefile
QMAKE         = /opt/QtSDK/Desktop/Qt/4.8.0/gcc/bin/qmake
DEL_FILE      = rm -f
CHK_DIR_EXISTS= test -d
MKDIR         = mkdir -p
COPY          = cp -f
COPY_FILE     = $(COPY)
COPY_DIR      = $(COPY) -r
INSTALL_FILE  = install -m 644 -p
INSTALL_PROGRAM = install -m 755 -p
INSTALL_DIR   = $(COPY_DIR)
DEL_FILE      = rm -f
SYMLINK       = ln -f -s
DEL_DIR       = rmdir
MOVE          = mv -f
CHK_DIR_EXISTS= test -d
MKDIR         = mkdir -p
SUBTARGETS    = 


Makefile: pyqt.pro  /opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/default/qmake.conf /opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/unix.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/linux.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/gcc-base.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/gcc-base-unix.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/g++-base.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/g++-unix.conf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/qconfig.pri \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/modules/qt_webkit_version.pri \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt_functions.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt_config.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/exclusive_builds.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/default_pre.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/release.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/default_post.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/unix/gdb_dwarf_index.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/warn_on.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/unix/thread.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/moc.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/resources.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/uic.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/yacc.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/lex.prf \
		/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/include_source_dir.prf
	$(QMAKE) -o Makefile pyqt.pro
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/unix.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/linux.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/gcc-base.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/gcc-base-unix.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/g++-base.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/common/g++-unix.conf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/qconfig.pri:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/modules/qt_webkit_version.pri:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt_functions.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt_config.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/exclusive_builds.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/default_pre.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/release.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/default_post.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/unix/gdb_dwarf_index.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/warn_on.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/qt.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/unix/thread.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/moc.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/resources.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/uic.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/yacc.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/lex.prf:
/opt/QtSDK/Desktop/Qt/4.8.0/gcc/mkspecs/features/include_source_dir.prf:
qmake: qmake_all FORCE
	@$(QMAKE) -o Makefile pyqt.pro

qmake_all: FORCE

make_default: FORCE
make_first: FORCE
all: FORCE
clean: FORCE
distclean: FORCE
	-$(DEL_FILE) Makefile
install_subtargets: FORCE
uninstall_subtargets: FORCE

check:

mocclean: compiler_moc_header_clean compiler_moc_source_clean

mocables: compiler_moc_header_make_all compiler_moc_source_make_all
install: install_subtargets  FORCE

uninstall:  uninstall_subtargets FORCE

FORCE:

