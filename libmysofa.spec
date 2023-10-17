%define major 1
%define libname %mklibname mysofa %{major}
%define devname %mklibname mysofa -d

Summary:	C library to read HRTFs if they are stored in the AES69-2015 SOFA format
Name:		libmysofa
Version:	1.3.2
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://github.com/hoene/libmysofa
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(cunit)
Requires:	%{libname} = %{EVRD}

%description
C library to read HRTFs if they are stored in the 
AES69-2015 SOFA format.

%files
%{_bindir}/mysofa2json
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/MIT_KEMAR_normal_pinna.sofa
%{_datadir}/%{name}/default.sofa

# -------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library files for libmysofa
Group:		System/Libraries

%description -n %{libname}
libmysofa library for ffmpeg.
This package contains the shared library file.

%files -n %{libname}
%{_libdir}/libmysofa.so.%{major}*

# -------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libmysofa
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
libmysofa library for ffmpeg.
This package contains the development files.

%files -n %{devname}
#{_includedir}/mysofa.h
%{_libdir}/libmysofa.so
%{_libdir}/pkgconfig/libmysofa.pc

# -------------------------------------------------------------------------

%prep
%autosetup -p1

sed -i 's|/lib|/%{_lib}/pkgconfig|g' libmysofa.pc.cmake
sed -i 's|lib/pkgconfig|%{_lib}/pkgconfig|g' CMakeLists.txt

%build
%cmake \
	-DBUILD_STATIC_LIBS=OFF \
	-DCODE_COVERAGE=OFF \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-G Ninja

%ninja_build

%install
%ninja_install -C build
