from app.ugc.models import Item, Profiler
import uuid
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


def get_user(update):
    char_id = update.message.chat_id
    p, _ = Profiler.objects.get_or_create(
        external_id=char_id,
        defaults={
            "name": update.message.from_user.username
        }
    )
    return p


def start_bot_callback(update, callbackcontext):
    p = get_user(update)
    update.message.reply_text(settings.TEXT_WELCOME + ", " + p.name + "!")


def show_item_callback(update, callbackcontext):
    items_info = []
    if len(callbackcontext.args) >= 1:
        for item in callbackcontext.args:
            items_info.append(str(Item.objects.get(name=item)))
            items_info.append("\n")
    else:
        for item in Item.objects.all():
            items_info.append(str(item))
            items_info.append("\n")
    update.message.reply_text("\n".join(items_info))


def create_item_callback(update, callbackcontext):
    if len(callbackcontext.args) >= 1:
        p = get_user(update)
        test = uuid.uuid4()
        item = Item(profiler=p, id=test)
        try:
            for param in callbackcontext.args:
                pair = param.split(sep='=')
                setattr(item, pair[0], pair[1])
        except AttributeError as ex:
            update.message.reply_text(str(ex))
        item.save()
        item = Item.objects
        update.message.reply_text("success, create id:")
        update.message.reply_text(str(test))
    else:
        update.message.reply_text(
            'Please, enter format item: [/create] [option]=[something] ...')


def update_item_callback(update, callbackcontext):
    if len(callbackcontext.args) >= 1:
        u = get_user(update)
        id = uuid.UUID(callbackcontext.args[0])
        item = Item.objects.get(profiler=u, id=id)
        for param in callbackcontext.args[1:]:
            pair = param.split(sep='=')
            setattr(item, pair[0], pair[1])
        item.save()
        update.message.reply_text("success changed")
    else:
        update.message.reply_text(
            'Please, enter format item: [/update] id [option]=[something] ...')


def delete_item_callback(update, callbackcontext):
    if len(callbackcontext.args) == 1:
        try:
            u = get_user(update)
            id = uuid.UUID(callbackcontext.args[0])
            item = Item.objects.get(profiler=u, id=id)
            item.delete()
            update.message.reply_text("success deleted")
        except ObjectDoesNotExist as ex:
            update.message.reply_text("Item not found")
    else:
        update.message.reply_text(
            'Please, enter format item: [/delete] id')


def unknown_command_callback(update, callbackcontext):
    update.message.reply_text(
        "Sorry, the command is not supported or not allowed.")
