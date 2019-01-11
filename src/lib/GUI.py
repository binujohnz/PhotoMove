# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainForm
###########################################################################

class MainForm ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Photo Matcher", pos = wx.DefaultPosition, size = wx.Size( 992,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 850,500 ), wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Inputs" ), wx.VERTICAL )

        sbSizer2.SetMinSize( wx.Size( -1,100 ) )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"\nSource Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer5.Add( self.m_staticText1, 0, 0, 5 )

        self.dpickSource = wx.DirPickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.dpickSource.SetMinSize( wx.Size( 500,-1 ) )

        bSizer5.Add( self.dpickSource, 0, wx.ALL, 5 )


        sbSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

        self.lblIroot = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Image Root:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblIroot.Wrap( -1 )

        sbSizer2.Add( self.lblIroot, 0, wx.ALL, 5 )

        self.lblVroot = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Video Root:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblVroot.Wrap( -1 )

        sbSizer2.Add( self.lblVroot, 0, wx.ALL, 5 )

        self.lblGroot = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Working: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblGroot.Wrap( -1 )

        sbSizer2.Add( self.lblGroot, 0, wx.ALL, 5 )


        bSizer14.Add( sbSizer2, 1, wx.EXPAND, 5 )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )

        rbSelectionChoices = [ u"Images", u"Videos", u"Both" ]
        self.rbSelection = wx.RadioBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, rbSelectionChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rbSelection.SetSelection( 2 )
        sbSizer3.Add( self.rbSelection, 0, wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.cbMove = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Delete Source file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cbMove.SetValue(True)
        gSizer3.Add( self.cbMove, 0, wx.ALL, 5 )

        self.cbOverwrite = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Overwrite if Already Exists!", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.cbOverwrite, 0, wx.ALL, 5 )


        sbSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )

        self.lblTypes = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"types goes here", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblTypes.Wrap( -1 )

        sbSizer3.Add( self.lblTypes, 0, wx.ALL, 5 )

        self.lblExcList = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"list of dir to exclude", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblExcList.Wrap( -1 )

        sbSizer3.Add( self.lblExcList, 0, wx.ALL, 5 )


        bSizer14.Add( sbSizer3, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer14, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.butCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.butCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.butCopy = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.butCopy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer4.Add( bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow2.SetScrollRate( 5, 5 )
        self.m_scrolledWindow2.SetMinSize( wx.Size( -1,500 ) )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )


        self.m_scrolledWindow2.SetSizer( bSizer7 )
        self.m_scrolledWindow2.Layout()
        bSizer7.Fit( self.m_scrolledWindow2 )
        bSizer8.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()
        self.stMain = self.CreateStatusBar( 3, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.menuFile = wx.Menu()
        self.mitOptions = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Options"+ u"\t" + u"Ctrl+o", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.mitOptions )

        self.mitLogs = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Open Log"+ u"\t" + u"Ctrl+l", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.mitLogs )

        self.menuFile.AppendSeparator()

        self.mitClose = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Close", u"Close Application", wx.ITEM_NORMAL )
        self.menuFile.Append( self.mitClose )

        self.m_menubar1.Append( self.menuFile, u"File" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.safeClose )
        self.butCancel.Bind( wx.EVT_BUTTON, self.cancelRun )
        self.butCopy.Bind( wx.EVT_BUTTON, self.startRun )
        self.Bind( wx.EVT_MENU, self.setOptions, id = self.mitOptions.GetId() )
        self.Bind( wx.EVT_MENU, self.openLogs, id = self.mitLogs.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def safeClose( self, event ):
        event.Skip()

    def cancelRun( self, event ):
        event.Skip()

    def startRun( self, event ):
        event.Skip()

    def setOptions( self, event ):
        event.Skip()

    def openLogs( self, event ):
        event.Skip()


###########################################################################
## Class diaLogs
###########################################################################

class diaLogs ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Photo Master - Logs", pos = wx.DefaultPosition, size = wx.Size( 662,401 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow6 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow6.SetScrollRate( 5, 5 )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.lblLog = wx.StaticText( self.m_scrolledWindow6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblLog.Wrap( -1 )

        bSizer12.Add( self.lblLog, 0, wx.ALL, 5 )


        self.m_scrolledWindow6.SetSizer( bSizer12 )
        self.m_scrolledWindow6.Layout()
        bSizer12.Fit( self.m_scrolledWindow6 )
        bSizer8.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_ACTIVATE, self.activate )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def activate( self, event ):
        event.Skip()


###########################################################################
## Class diaOptions
###########################################################################

class diaOptions ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Set Options", pos = wx.DefaultPosition, size = wx.Size( 482,434 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Destination Paths" ), wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Image Destination: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        sbSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.dpickImgDest = wx.DirPickerCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.dpickImgDest.SetMinSize( wx.Size( 450,-1 ) )

        sbSizer4.Add( self.dpickImgDest, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Video Destination:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        sbSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.dpickVideos = wx.DirPickerCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.dpickVideos.SetMinSize( wx.Size( 450,-1 ) )

        sbSizer4.Add( self.dpickVideos, 0, wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Duplicates:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        sbSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )

        self.dpickDup = wx.DirPickerCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.dpickDup.SetMinSize( wx.Size( 450,-1 ) )

        sbSizer4.Add( self.dpickDup, 0, wx.ALL, 5 )

        self.mylabel232 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Exclude Dir Patterns:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.mylabel232.Wrap( -1 )

        sbSizer4.Add( self.mylabel232, 0, wx.ALL, 5 )

        self.txtExcDirs = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, u".Thumbnails,.Metadata", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtExcDirs.SetToolTip( u"Comma Separated list of Directory names to exclude" )
        self.txtExcDirs.SetMinSize( wx.Size( 400,-1 ) )
        self.txtExcDirs.SetMaxSize( wx.Size( 400,-1 ) )

        sbSizer4.Add( self.txtExcDirs, 0, wx.ALL, 5 )

        self.m_staticText161 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Destination Dir Naming Pattern", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText161.Wrap( -1 )

        sbSizer4.Add( self.m_staticText161, 0, wx.ALL, 5 )

        self.txtDirFormat = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtDirFormat.SetMinSize( wx.Size( 400,-1 ) )

        sbSizer4.Add( self.txtDirFormat, 0, wx.ALL, 5 )


        bSizer16.Add( sbSizer4, 1, wx.EXPAND, 5 )

        gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

        self.butCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer13.Add( self.butCancel, 0, wx.ALL, 5 )

        self.butUpdate = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer13.Add( self.butUpdate, 0, wx.ALL, 5 )


        bSizer16.Add( gSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer16 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_ACTIVATE_APP, self.optionsLoad )
        self.butCancel.Bind( wx.EVT_BUTTON, self.cancelOpt )
        self.butUpdate.Bind( wx.EVT_BUTTON, self.updateOpt )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def optionsLoad( self, event ):
        event.Skip()

    def cancelOpt( self, event ):
        event.Skip()

    def updateOpt( self, event ):
        event.Skip()


