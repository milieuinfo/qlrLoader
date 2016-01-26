
SOURCES = __init__.py qlrLoader.py

PLUGINNAME = qlrLoader

PY_FILES = __init__.py qlrLoader.py

#UI_FILES =

EXTRAS = metadata.txt icon.png

RESOURCE_FILES = resources_rc.py

QGISDIR=.qgis2

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%_rc.py : %.qrc
	pyrcc4 -o $*_rc.py  $<

%.py : %.ui
	#pyuic4 -o $@ $<
	python C:\OSGeo4W64\apps\Python27\lib\site-packages\PyQt4\uic\pyuic.py -o $@ $<

deploy: compile
	if [ -d "$(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)" ]; then rm -r $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME); fi
	mkdir -p $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
#	cp -vf $(UI_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vfr $(EXTRAS) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)

dclean:
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname "*.pyc" -delete
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname ".git" -prune -exec rm -Rf {} \;

derase:
	rm -Rf $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)

zip: deploy
	rm -f build/$(PLUGINNAME).zip
	cd $(HOME)/$(QGISDIR)/python/plugins; zip -9r $(CURDIR)/build/$(PLUGINNAME).zip $(PLUGINNAME)

package: compile
	rm -f $(PLUGINNAME).zip
	git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(VERSION)
	echo "Created package: $(PLUGINNAME).zip"

upload: zip
	$(PLUGIN_UPLOAD) $(PLUGINNAME).zip

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)

