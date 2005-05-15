Summary:	Bing, a point-to-point bandwidth measurement tool (b from Bandwith)
Summary(pl):	Bing, narzêdzie s³u¿±ce mierzeniu przepustowo¶ci ³±czy
Name:		bing
Version:	1.1.3
Release:	3
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.fibrespeed.net/~mbabcock/mirrors/bing/%{name}-%{version}.tar.bz2
# Source0-md5:	095f8a04f37df2ed5c99328ddc551a09
Patch0:		%{name}.patch
URL:		http://web.cnam.fr/reseau/bing.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%description -l pl
Bing oblicza aktualn± (w przeciwieñstwie do np. ¶redniej) przepustowo¶æ 
³±cza mierz±c czasy powrotu odpowiedzi na komunikaty ICMP.

%prep
%setup -q
%patch -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install bing $RPM_BUILD_ROOT%{_bindir}
install unix/bing.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Readme.*
%attr(755,root,root) %{_bindir}/bing
%{_mandir}/man8/bing.8*
