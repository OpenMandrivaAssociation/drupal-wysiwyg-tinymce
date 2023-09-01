%define oname	tinymce

Name:		drupal-wysiwyg-tinymce
Summary:	TinyMCE editor for Drupal Wysiwyg module
Version:	6.7.0
Release:	1
License:	LGPLv2.1
Group:		Networking/WWW
URL:		http://www.tinymce.com/
Source0:	https://github.com/tinymce/tinymce/archive/refs/tags/%{version}.tar.gz
Requires:	drupal-wysiwyg
Provides:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
TinyMCE is a platform independent web based Javascript HTML WYSIWYG editor
control released as Open Source under LGPL by Moxiecode Systems AB.

TinyMCE has the ability to convert HTML TEXTAREA fields or other HTML elements
to editor instances. TinyMCE is very easy to integrate into other Content
Management Systems.

%prep
%autosetup -p1 -n tinymce-%{version}

%build

%install
%__install -d %{buildroot}/srv/www/drupal//sites/all/libraries/
cp -a . %{buildroot}/srv/www/drupal//sites/all/libraries/%{oname}
rm %{buildroot}/srv/www/drupal//sites/all/libraries/%{oname}/*.txt

%files
/srv/www/drupal//sites/all/libraries/%{oname}
