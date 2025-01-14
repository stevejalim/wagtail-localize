# Generated by Django 4.1.9 on 2023-05-24 15:10

import wagtail.blocks
import wagtail.blocks.field_block
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks

from django.db import migrations

import wagtail_localize.test.models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_localize_test", "0002_header_navigationlink_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testgeneratetranslatablefieldspage",
            name="test_streamfield",
            field=wagtail.fields.StreamField(
                [
                    ("test_charblock", wagtail.blocks.CharBlock(max_length=255)),
                    ("test_textblock", wagtail.blocks.TextBlock(label="text block")),
                    ("test_emailblock", wagtail.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.blocks.ListBlock(wagtail.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.blocks.ListBlock(
                                                        wagtail.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.blocks.TextBlock()),
                                ("block_b", wagtail.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            ("page", wagtail.blocks.PageChooserBlock()),
                                            (
                                                "checklist",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.blocks.StructBlock(
                            [("page", wagtail.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(required=False),
                                    )
                                ]
                            )
                        ),
                    ),
                    (
                        "test_image_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "test_document_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.documents.blocks.DocumentChooserBlock()
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_list_in_stream_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StreamBlock(
                                [
                                    (
                                        "list",
                                        wagtail.blocks.ListBlock(
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "page",
                                                        wagtail.blocks.PageChooserBlock(
                                                            required=False
                                                        ),
                                                    )
                                                ]
                                            )
                                        ),
                                    )
                                ]
                            )
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="testpage",
            name="test_streamfield",
            field=wagtail.fields.StreamField(
                [
                    ("test_charblock", wagtail.blocks.CharBlock(max_length=255)),
                    ("test_textblock", wagtail.blocks.TextBlock(label="text block")),
                    ("test_emailblock", wagtail.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.blocks.ListBlock(wagtail.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.blocks.ListBlock(
                                                        wagtail.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.blocks.TextBlock()),
                                ("block_b", wagtail.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            ("page", wagtail.blocks.PageChooserBlock()),
                                            (
                                                "checklist",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.blocks.StructBlock(
                            [("page", wagtail.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(required=False),
                                    )
                                ]
                            )
                        ),
                    ),
                    (
                        "test_image_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "test_document_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.documents.blocks.DocumentChooserBlock()
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_list_in_stream_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StreamBlock(
                                [
                                    (
                                        "list",
                                        wagtail.blocks.ListBlock(
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "page",
                                                        wagtail.blocks.PageChooserBlock(
                                                            required=False
                                                        ),
                                                    )
                                                ]
                                            )
                                        ),
                                    )
                                ]
                            )
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="testpage",
            name="test_synchronized_streamfield",
            field=wagtail.fields.StreamField(
                [
                    ("test_charblock", wagtail.blocks.CharBlock(max_length=255)),
                    ("test_textblock", wagtail.blocks.TextBlock(label="text block")),
                    ("test_emailblock", wagtail.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.blocks.ListBlock(wagtail.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.blocks.ListBlock(
                                                        wagtail.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.blocks.TextBlock()),
                                ("block_b", wagtail.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            ("page", wagtail.blocks.PageChooserBlock()),
                                            (
                                                "checklist",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                ("field_a", wagtail.blocks.TextBlock()),
                                ("field_b", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.blocks.StructBlock(
                            [("page", wagtail.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.blocks.StructBlock(
                                        [("page", wagtail.blocks.PageChooserBlock())]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(required=False),
                                    )
                                ]
                            )
                        ),
                    ),
                    (
                        "test_image_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "test_document_chooser_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.documents.blocks.DocumentChooserBlock()
                        ),
                    ),
                    (
                        "test_chooser_in_struct_in_list_in_stream_in_listblock",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StreamBlock(
                                [
                                    (
                                        "list",
                                        wagtail.blocks.ListBlock(
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "page",
                                                        wagtail.blocks.PageChooserBlock(
                                                            required=False
                                                        ),
                                                    )
                                                ]
                                            )
                                        ),
                                    )
                                ]
                            )
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
